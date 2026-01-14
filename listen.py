import speech_recognition as sr
import sys

def listen_command(mic_idx):
    """
    Captures audio from the microphone and converts it to text.
    Accepts mic_idx from main.py to ensure it uses the correct hardware.
    """
    r = sr.Recognizer()
    
    # These settings help Jarvis ignore background noise on the Pi
    r.energy_threshold = 400 
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8  # Seconds of silence before it stops recording

    try:
        # We use the 'with' statement to ensure the microphone 
        # is released as soon as this block finishes.
        with sr.Microphone(device_index=mic_idx) as source:
            # Short calibration for better accuracy
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            print("Jarvis: Listening for command...")
            # timeout: stops waiting for speech after 5 seconds
            # phrase_time_limit: cuts off long talking after 10 seconds
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
        print("Jarvis: Processing speech...")
        # Convert audio to text using Google's free API
        command = r.recognize_google(audio)
        return command.lower()

    except sr.WaitTimeoutError:
        # Triggered if no one says anything within 5 seconds
        return None
    except sr.UnknownValueError:
        # Triggered if Jarvis hears noise but can't find words
        return None
    except Exception as e:
        # sys.__stderr__ ensures you see hardware errors even if logs are silenced
        sys.__stderr__.write(f"Speech Recognition Error: {e}\n")
        return None
