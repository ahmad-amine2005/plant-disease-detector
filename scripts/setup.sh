#!/bin/bash
set -e

echo "🌿 Plant Disease Detector — Setup"
echo "====================================="

# Backend
echo "\n📦 Setting up Python backend..."
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✅ Backend dependencies installed."
cd ..

# Frontend
echo "\n📦 Setting up Next.js frontend..."
cd frontend
npm install --silent
echo "✅ Frontend dependencies installed."
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Copy model weights to backend/models/"
echo "  2. Run: cd backend && python model_converter.py"
echo "  3. Start backend: cd backend && uvicorn main:app --port 8000"
echo "  4. Start frontend: cd frontend && npm run dev"
echo "  5. Open http://localhost:3000"
