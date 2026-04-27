"""Model loading & inference — supports TFLite (preferred) and fallback Keras."""
from __future__ import annotations

import logging
import os
from pathlib import Path

import numpy as np
from PIL import Image

log = logging.getLogger("plant-inference")

CLASS_LABELS = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy", "Cherry_(including_sour)___Powdery_mildew", "Cherry___healthy",
    "Corn___Cercospora_leaf_spot_Gray_leaf_spot", "Corn___Common_rust", "Corn___Northern_Leaf_Blight",
    "Corn___healthy", "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot", "Peach___healthy",
    "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy", "Potato___Early_blight",
    "Potato___Late_blight", "Potato___healthy", "Raspberry___healthy", "Soybean___healthy",
    "Squash___Powdery_mildew", "Strawberry___Leaf_scorch", "Strawberry___healthy",
    "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight", "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites_Two-spotted_spider_mite",
    "Tomato___Target_Spot", "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]

IMG_SIZE = (224, 224)


class PlantDiseaseClassifier:
    def __init__(
        self,
        tflite_path: str = "models/plant_disease_model_int8.tflite",
        json_path: str = "models/global_mobilenet_pv_pv_white.json",
        weights_path: str = "models/global_mobilenet_pv_pv_white.h5",
        use_tflite: bool = True,
    ):
        self._use_tflite = use_tflite and Path(tflite_path).exists()
        if self._use_tflite:
            self._load_tflite(tflite_path)
            log.info("Using TFLite model: %s", tflite_path)
        else:
            self._load_keras(json_path, weights_path)
            log.info("Using Keras model (fallback)")

    # ------------------------------------------------------------------
    # Loaders
    # ------------------------------------------------------------------

    def _load_tflite(self, path: str) -> None:
        try:
            import tflite_runtime.interpreter as tflite
            self._interpreter = tflite.Interpreter(
                model_path=path,
                num_threads=min(4, os.cpu_count() or 1),
            )
        except ImportError:
            import tensorflow as tf
            self._interpreter = tf.lite.Interpreter(
                model_path=path,
                num_threads=min(4, os.cpu_count() or 1),
            )
        self._interpreter.allocate_tensors()
        self._input_details = self._interpreter.get_input_details()
        self._output_details = self._interpreter.get_output_details()
        self._is_quantized = self._input_details[0]["dtype"] == np.int8

    def _load_keras(self, json_path: str, weights_path: str) -> None:
        os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
        import tensorflow as tf
        with open(json_path) as f:
            self._keras_model = tf.keras.models.model_from_json(f.read())
        self._keras_model.load_weights(weights_path)
        log.info("Keras model loaded from disk")

    # ------------------------------------------------------------------
    # Preprocessing
    # ------------------------------------------------------------------

    def _preprocess(self, img: Image.Image) -> np.ndarray:
        img = img.resize(IMG_SIZE, Image.LANCZOS)
        arr = np.array(img, dtype=np.float32) / 255.0  # [0, 1]
        return np.expand_dims(arr, axis=0)  # (1, 224, 224, 3)

    # ------------------------------------------------------------------
    # Inference
    # ------------------------------------------------------------------

    def predict(self, img: Image.Image) -> tuple[str, float, list[tuple[str, float]]]:
        """Returns (top_label, top_confidence, [(label, confidence) x3])."""
        if self._use_tflite:
            return self._predict_tflite(img)
        return self._predict_keras(img)

    def _predict_tflite(self, img: Image.Image):
        arr = self._preprocess(img)
        if self._is_quantized:
            scale, zero_point = self._input_details[0]["quantization"]
            arr = (arr / scale + zero_point).astype(np.int8)
        self._interpreter.set_tensor(self._input_details[0]["index"], arr)
        self._interpreter.invoke()
        output = self._interpreter.get_tensor(self._output_details[0]["index"])[0]
        if self._is_quantized:
            out_scale, out_zero = self._output_details[0]["quantization"]
            output = (output.astype(np.float32) - out_zero) * out_scale
        probs = _softmax(output.astype(np.float32))
        return _top_results(probs)

    def _predict_keras(self, img: Image.Image):
        arr = self._preprocess(img)
        probs = self._keras_model.predict(arr, verbose=0)[0]
        return _top_results(probs)


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _softmax(x: np.ndarray) -> np.ndarray:
    e = np.exp(x - x.max())
    return e / e.sum()


def _top_results(probs: np.ndarray, k: int = 3):
    top_idx = np.argsort(probs)[::-1][:k]
    top3 = [(CLASS_LABELS[i], float(probs[i])) for i in top_idx]
    label, confidence = top3[0]
    return label, confidence, top3
