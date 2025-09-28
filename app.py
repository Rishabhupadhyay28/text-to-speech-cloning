from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
import os, uuid
from src.tts_engine import text_to_speech
from src.voice_cloning import clone_voice
from src.preprocessing import preprocess_audio
from config.settings import OUTPUT_DIR, SAMPLES_DIR
from src.utils import ensure_dirs

app = FastAPI(title="TTS + Voice Cloning API")

# Ensure directories exist
ensure_dirs([OUTPUT_DIR, SAMPLES_DIR])

@app.get("/")
async def root():
    return {"message": "✅ TTS + Voice Cloning API is running!"}

@app.post("/tts/")
async def generate_tts(
    text: str = Form(...),
    speaker: str = Form(None),
    language: str = Form(None)
):
    """
    Generate speech from text.
    """
    filename = f"tts_{uuid.uuid4().hex}.wav"
    output = text_to_speech(text, filename)
    return FileResponse(output, media_type="audio/wav")

@app.post("/clone/")
async def generate_clone(
    text: str = Form(...),
    file: UploadFile = None
):
    """
    Clone voice using an uploaded sample file.
    """
    # Save uploaded file
    input_path = os.path.join(SAMPLES_DIR, file.filename)
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Preprocess into new file
    processed_path = os.path.join(SAMPLES_DIR, f"processed_{file.filename}.wav")
    processed = preprocess_audio(input_path, processed_path)

    # Run cloning
    filename = f"clone_{uuid.uuid4().hex}.wav"
    output = clone_voice(text, processed, filename)

    return FileResponse(output, media_type="audio/wav")
