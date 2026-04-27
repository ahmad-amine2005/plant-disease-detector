"""FastAPI inference server for Plant Disease Detection."""
from __future__ import annotations

import io
import logging
import os
import time
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image

from disease_info import DISEASE_INFO
from inference import PlantDiseaseClassifier

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(name)s | %(message)s")
log = logging.getLogger("plant-api")

# ---------------------------------------------------------------------------
# Global classifier instance (loaded once at startup)
# ---------------------------------------------------------------------------
classifier: PlantDiseaseClassifier | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global classifier
    log.info("Loading model ...")
    t0 = time.perf_counter()
    classifier = PlantDiseaseClassifier(
        tflite_path=os.getenv("MODEL_PATH", "models/plant_disease_model_int8.tflite"),
        json_path=os.getenv("MODEL_JSON", "models/global_mobilenet_pv_pv_white.json"),
        weights_path=os.getenv("MODEL_WEIGHTS", "models/global_mobilenet_pv_pv_white.h5"),
        use_tflite=os.getenv("USE_TFLITE", "true").lower() == "true",
    )
    log.info("Model ready in %.2fs", time.perf_counter() - t0)
    yield
    log.info("Shutting down.")


app = FastAPI(
    title="Plant Disease Detector API",
    description="Local CPU-optimised plant disease detection via TFLite MobileNet.",
    version="1.0.0",
    lifespan=lifespan,
)

allowed_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp", "image/jpg"}
MAX_IMAGE_SIZE = int(os.getenv("MAX_IMAGE_SIZE", 500))


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": classifier is not None}


@app.get("/classes")
async def list_classes():
    """Return all 38 supported disease / healthy class labels."""
    return {"classes": list(DISEASE_INFO.keys())}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if classifier is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet. Please retry.")

    # ---------- validate ----------
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=415,
            detail=f"Unsupported file type '{file.content_type}'. Upload JPEG, PNG, or WebP.",
        )

    raw = await file.read()
    if len(raw) > 10 * 1024 * 1024:  # 10 MB hard cap
        raise HTTPException(status_code=413, detail="File too large. Maximum is 10 MB.")

    # ---------- pre-process ----------
    try:
        img = Image.open(io.BytesIO(raw)).convert("RGB")
        if img.width > MAX_IMAGE_SIZE or img.height > MAX_IMAGE_SIZE:
            img = img.resize((MAX_IMAGE_SIZE, MAX_IMAGE_SIZE), Image.LANCZOS)
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Cannot read image: {exc}")

    # ---------- infer ----------
    t0 = time.perf_counter()
    try:
        label, confidence, top3 = classifier.predict(img)
    except Exception as exc:
        log.exception("Inference error")
        raise HTTPException(status_code=500, detail=f"Inference failed: {exc}")
    elapsed_ms = round((time.perf_counter() - t0) * 1000, 1)

    info = DISEASE_INFO.get(label, {})
    plant, condition = _split_label(label)

    return JSONResponse({
        "label": label,
        "plant": plant,
        "condition": condition,
        "is_healthy": "healthy" in label.lower(),
        "confidence": round(float(confidence) * 100, 1),
        "top3": [{"label": l, "confidence": round(float(c) * 100, 1)} for l, c in top3],
        "description": info.get("description", ""),
        "recommendations": info.get("recommendations", []),
        "severity": info.get("severity", "unknown"),
        "inference_ms": elapsed_ms,
    })


def _split_label(label: str) -> tuple[str, str]:
    """'Tomato___Early_blight' -> ('Tomato', 'Early Blight')"""
    parts = label.split("___", 1)
    plant = parts[0].replace("_", " ").replace(",", "").strip()
    condition = parts[1].replace("_", " ").strip().title() if len(parts) > 1 else "Unknown"
    return plant, condition
