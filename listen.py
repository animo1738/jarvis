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

import speech_recognition as sr

def find_mic_index():
    devices = PvRecorder.get_available_devices()
    for i, device in enumerate(devices):
        name = device.lower()
        if ("usb" in name or "fifine" in name) and "monitor" not in name:
            print(f"Found Microphone at Index {i}: {device}")
            return i
    for i, device in enumerate(devices):
        if "monitor" not in device.lower():
            return i
    return None

def listen(mic_index=2):
    r = sr.Recognizer()
    
    audio = None 
    
    try:
       
        with sr.Microphone(device_index=mic_index, sample_rate=16000) as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            print(f"Listening on Index {mic_index}...")
            
            # This is where it used to crash. 
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
        if audio:
            print("Done listening, recognizing...")
            return r.recognize_google(audio)
            
    except Exception as e:
        
        print(f"Hardware Error: {e}")
        return None

    return None
