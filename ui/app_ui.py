import streamlit as st
import requests
import os

API_URL = "http://127.0.0.1:8000"

st.title("🎙️ TTS + Voice Cloning")

# ---- TTS Section ----
st.header("Text to Speech")
text_input = st.text_area("Enter text to synthesize:")
if st.button("Generate Speech"):
    if text_input.strip():
        response = requests.post(f"{API_URL}/tts/", data={"text": text_input})
        if response.status_code == 200:
            output_file = "tts_output.wav"
            with open(output_file, "wb") as f:
                f.write(response.content)
            st.audio(output_file, format="audio/wav")
            st.success("✅ Speech generated successfully!")
        else:
            st.error("❌ Failed to generate TTS.")

# ---- Voice Cloning Section ----
st.header("Voice Cloning")
clone_text = st.text_area("Enter text to clone with your voice:")
voice_file = st.file_uploader("Upload voice sample (wav, m4a, mp3)", type=["wav", "m4a", "mp3"])

if st.button("Clone My Voice"):
    if clone_text.strip() and voice_file:
        files = {"file": (voice_file.name, voice_file, voice_file.type)}
        data = {"text": clone_text}
        response = requests.post(f"{API_URL}/clone/", data=data, files=files)

        if response.status_code == 200:
            output_file = "cloned_output.wav"
            with open(output_file, "wb") as f:
                f.write(response.content)
            st.audio(output_file, format="audio/wav")
            st.success("✅ Voice cloned successfully!")
        else:
            st.error("❌ Failed to clone voice.")
