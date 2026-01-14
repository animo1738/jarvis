import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    # Higher energy threshold helps ignore background static
    r.energy_threshold = 600 
    
    try:
        # No device_index needed; PulseAudio handles the 'default'
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            
            print("Recognizing...")
            return r.recognize_google(audio)
    except Exception as e:
        return None
