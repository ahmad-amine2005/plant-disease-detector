"""One-time converter: Keras (.json + .h5)  ->  TFLite INT8.

Usage:
    cd backend
    python model_converter.py

Outputs:
    models/plant_disease_model_int8.tflite
"""
from __future__ import annotations

import logging
import os
import pathlib
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger("converter")

MODEL_JSON = "models/global_mobilenet_pv_pv_white.json"
MODEL_WEIGHTS = "models/global_mobilenet_pv_pv_white.h5"
OUTPUT_TFLITE = "models/plant_disease_model_int8.tflite"
IMG_SIZE = (224, 224)
NUM_CALIBRATION_SAMPLES = 200


def load_keras_model():
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    import tensorflow as tf
    log.info("Loading Keras model from JSON + H5 ...")
    with open(MODEL_JSON) as f:
        model = tf.keras.models.model_from_json(f.read())
    model.load_weights(MODEL_WEIGHTS)
    log.info("Keras model loaded. Parameters: {:,}".format(model.count_params()))
    return model


def representative_dataset():
    """Generate synthetic representative data for INT8 calibration."""
    rng = np.random.default_rng(42)
    for _ in range(NUM_CALIBRATION_SAMPLES):
        sample = rng.uniform(0, 1, (1, IMG_SIZE[0], IMG_SIZE[1], 3)).astype(np.float32)
        yield [sample]


def convert(model) -> bytes:
    import tensorflow as tf
    log.info("Converting to TFLite with INT8 post-training quantization ...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.representative_dataset = representative_dataset
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    converter.inference_input_type = tf.int8
    converter.inference_output_type = tf.int8
    tflite_model = converter.convert()
    log.info("Conversion complete. Model size: {:.1f} MB".format(len(tflite_model) / 1e6))
    return tflite_model


def main():
    pathlib.Path("models").mkdir(exist_ok=True)
    model = load_keras_model()
    tflite_bytes = convert(model)
    with open(OUTPUT_TFLITE, "wb") as f:
        f.write(tflite_bytes)
    log.info("Saved: %s", OUTPUT_TFLITE)
    log.info("Done! You can now start the server with: uvicorn main:app --port 8000")


if __name__ == "__main__":
    main()
