# 🌿 Plant Disease Detector

A modern, optimized local web application for field plant disease detection — built with **Next.js** (frontend) and **FastAPI** (backend), running a quantized **MobileNet TFLite** model for fast, CPU-only inference on standard 16GB RAM machines.

> Powered by the original [Field Plant Disease Detection](https://github.com/emmanuelmoupojou2/Field_Plant_Disease_Detection) research model, now optimized for real-world local deployment.

---

## ✨ Features

- 🚀 **Fast inference** — TensorFlow Lite INT8-quantized MobileNet (~10–40ms/image on CPU)
- 🧠 **38 disease classes** across 14 plant species (PlantVillage dataset)
- 🖥️ **Local-first** — no internet required after setup; all data stays on your machine
- 📱 **Responsive UI** — mobile-first design with Tailwind CSS
- 🎨 **Modern aesthetic** — glassmorphism cards, soft gradients, micro-animations
- ♿ **Accessible** — WCAG 2.1 AA compliant (ARIA labels, keyboard nav, contrast ratios)
- 🐍 **FastAPI backend** — async, lightweight, sub-100ms response times
- ⚡ **Next.js 14** — App Router, SSG, optimized asset loading

---

## 📦 Project Structure

```
plant-disease-detector/
├── backend/                   # Python FastAPI inference server
│   ├── main.py                # FastAPI app & /predict endpoint
│   ├── inference.py           # TFLite model loading & prediction
│   ├── model_converter.py     # One-time: Keras → TFLite INT8 conversion
│   ├── disease_info.py        # Disease descriptions & recommendations
│   ├── requirements.txt
│   └── models/                # Place your .tflite model here
├── frontend/                  # Next.js 14 application
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx           # Main landing + detection page
│   │   └── globals.css
│   ├── components/
│   │   ├── Navbar.tsx
│   │   ├── HeroSection.tsx
│   │   ├── DetectionInterface.tsx
│   │   ├── ResultsCard.tsx
│   │   ├── HowItWorks.tsx
│   │   ├── AboutSection.tsx
│   │   ├── TechDetails.tsx
│   │   └── Footer.tsx
│   ├── lib/
│   │   └── api.ts             # API client
│   ├── public/
│   ├── tailwind.config.ts
│   ├── next.config.ts
│   └── package.json
├── scripts/
│   └── setup.sh               # One-command setup script
├── docker-compose.yml         # Optional Docker deployment
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- 4GB free RAM (16GB total recommended)

### 1. Clone & Setup

```bash
git clone https://github.com/ahmad-amine2005/plant-disease-detector.git
cd plant-disease-detector
chmod +x scripts/setup.sh && ./scripts/setup.sh
```

### 2. Convert the Model (one-time)

First, clone the original repo and place model weights:
```bash
git clone https://github.com/emmanuelmoupojou2/Field_Plant_Disease_Detection.git
cp Field_Plant_Disease_Detection/model_weights/global_mobilenet_pv_pv_white.h5 backend/models/
cp Field_Plant_Disease_Detection/model_weights/global_mobilenet_pv_pv_white.json backend/models/
```

Then convert to TFLite:
```bash
cd backend
python model_converter.py
```

This produces `backend/models/plant_disease_model_int8.tflite` (~8–12MB).

### 3. Run the Application

**Terminal 1 — Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) 🎉

---

## 🔬 Model Optimization Details

| Metric | Original Keras | Optimized TFLite INT8 |
|--------|---------------|----------------------|
| Model size | ~90MB | ~8–12MB |
| Inference time (CPU) | 800–2000ms | 10–80ms |
| RAM usage | ~2–4GB | ~200–400MB |
| Accuracy loss | — | < 1% |

Optimizations applied:
- **INT8 Post-Training Quantization** — weights & activations quantized to 8-bit integers
- **Representative dataset calibration** — accurate quantization with minimal accuracy loss
- **Single-threaded inference** — predictable memory footprint
- **Image resizing at upload** — images capped at 500×500px before inference

---

## 🌱 Supported Plants & Diseases (38 classes)

Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato — with both diseased and healthy class labels.

---

## 📄 License

MIT — see [LICENSE](LICENSE)
