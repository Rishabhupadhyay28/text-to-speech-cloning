import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(DATA_DIR, "outputs")
SAMPLES_DIR = os.path.join(DATA_DIR, "samples")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Pretrained TTS model (Coqui)
TTS_MODEL_NAME = "tts_models/multilingual/multi-dataset/your_tts"
