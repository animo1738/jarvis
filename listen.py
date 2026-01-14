import speech_recognition as sr
import os

recognizer = sr.Recognizer()

def find_mic_index():
    # (Same find_mic_index function as above)
    pass

def listen(mic_index=2):
    r = sr.Recognizer()
    mic_idx = find_mic_index()
    if mic_idx is None:
        mic_idx = 3
        
    try:
        with sr.Microphone(device_index=mic_idx, sample_rate=16000) as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            print(f"Listening on Index {mic_idx}...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
        if audio:
            print("Done listening, recognizing...")
            return r.recognize_google(audio)
            
    except Exception as e:
        print(f"Hardware Error: {e}")
        return None
    return None
