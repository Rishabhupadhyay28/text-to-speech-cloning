from src.voice_cloning import clone_voice

# Path to your converted WAV sample
voice_sample = "data/samples/your_sample1.wav"

# Run voice cloning
path = clone_voice(
    text="My name is Ritika ,This is my cloned voice speaking. Welcome to the project!",
    speaker_wav=voice_sample,
    output_file="cloned_test.wav"
)

print("Generated cloned voice:", path)
