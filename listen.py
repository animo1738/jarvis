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

def listen(mic_index=2):
    r = sr.Recognizer()
    
    try:
        # Use the same index and force 16kHz (Standard for Voice AI)
        with sr.Microphone(device_index=mic_index, sample_rate=16000) as source:
            # Shorten duration for faster response in your video
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening for command...")
            
            # Timeout prevents the script from hanging forever
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
        print("Processing...")
        return r.recognize_google(audio)
        
    except sr.WaitTimeoutError:
        return None
    except Exception as e:
        print(f"STT Error: {e}")
        return None
