from TTS.api import TTS
from config.settings import TTS_MODEL_NAME, OUTPUT_DIR
import os

# Load TTS model once
tts = TTS(TTS_MODEL_NAME)

def text_to_speech(text: str, output_file: str = "output.wav"):
    """
    Convert text to speech with a default speaker & language.
    """
    # Ensure output folder exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # List available speakers and languages
    speakers = tts.speakers
    languages = tts.languages if hasattr(tts, "languages") else []

    print("Available speakers:", speakers)
    print("Available languages:", languages)

    # Pick safe defaults
    default_speaker = speakers[0] if speakers else None
    default_language = languages[0] if languages else None

    output_path = os.path.join(OUTPUT_DIR, output_file)

    # Run synthesis
    tts.tts_to_file(
        text=text,
        speaker=default_speaker,
        language=default_language,
        file_path=output_path
    )

    print(f"✅ Audio saved at: {output_path}")
    return output_path
