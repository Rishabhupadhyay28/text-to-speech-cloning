from pydub import AudioSegment

# Input .m4a file
input_file = "data/samples/your_recording.m4a"
output_file = "data/samples/your_sample.wav"

# Load and export as wav
sound = AudioSegment.from_file(input_file, format="m4a")
sound.export(output_file, format="wav")

print(f"✅ Converted: {output_file}")
