import speech_recognition as sr
import sys

def listen_command(mic_idx):
    r = sr.Recognizer()
    
    # We use 'with' to auto-close the mic immediately after use
    try:
        with sr.Microphone(device_index=mic_idx) as source:
            # Faster calibration to keep the response snappy
            r.adjust_for_ambient_noise(source, duration=0.5) 
            print("Jarvis: Listening for command...")
            
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            
            print("Jarvis: Recognizing...")
            return r.recognize_google(audio)
            
    except sr.UnknownValueError:
        return None # Could not understand audio
    except Exception as e:
        sys.__stderr__.write(f"Command Listen Error: {e}\n")
        return None
