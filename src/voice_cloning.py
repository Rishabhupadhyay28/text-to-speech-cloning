from TTS.api import TTS
from config.settings import TTS_MODEL_NAME, OUTPUT_DIR
import os
from pydub import AudioSegment

# Load model
tts = TTS(TTS_MODEL_NAME)

def clone_voice(text: str, speaker_wav: str, output_file: str = "cloned.wav"):
    """
    Generate speech in the style of a provided voice sample.
    Supports .wav, .mp3, and .m4a automatically.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # If file is m4a, convert to wav
    if speaker_wav.lower().endswith(".m4a"):
        temp_wav = speaker_wav.replace(".m4a", ".wav")
        sound = AudioSegment.from_file(speaker_wav, format="m4a")
        sound.export(temp_wav, format="wav")
        speaker_wav = temp_wav
        print(f"Converted M4A to WAV → {speaker_wav}")

    # Get defaults
    speakers = tts.speakers
    languages = tts.languages if hasattr(tts, "languages") else []
    default_speaker = speakers[0] if speakers else None
    default_language = languages[0] if languages else None

    output_path = os.path.join(OUTPUT_DIR, output_file)

    # Run synthesis
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        speaker=default_speaker,
        language=default_language,
        file_path=output_path
    )

    print(f"✅ Cloned voice saved at: {output_path}")
    return output_path
