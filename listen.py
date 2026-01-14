import speech_recognition as sr
import requests
import os
import tempfile

HF_TOKEN = os.getenv("HF_TOKEN")
WHISPER_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone(device_index=2) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as f:
            f.write(audio.get_wav_data())
            f.flush()

            response = requests.post(
                WHISPER_URL,
                headers=HEADERS,
                data=open(f.name, "rb")
            )

        if response.status_code != 200:
            print("Whisper API error:", response.text)
            return ""

        text = response.json().get("text", "").strip().lower()
        print("Heard:", text)
        return text

    except Exception as e:
        print("Listen error:", e)
        return ""
