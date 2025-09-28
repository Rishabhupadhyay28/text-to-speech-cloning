import librosa
import soundfile as sf
import os

def preprocess_audio(input_path: str, output_path: str, target_sr: int = 22050):
    """
    Normalize and resample user-uploaded audio.
    """
    audio, sr = librosa.load(input_path, sr=None)
    audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
    sf.write(output_path, audio, target_sr)
    return output_path
