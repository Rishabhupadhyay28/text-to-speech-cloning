from src.tts_engine import text_to_speech

# Call the function
path = text_to_speech("Hello, testing again!", output_file="test.wav")

print("Generated:", path)
