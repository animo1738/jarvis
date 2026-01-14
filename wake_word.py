import pvporcupine
from pvrecorder import PvRecorder
import os

def find_mic_index():
    # Use the class method directly
    devices = PvRecorder.get_available_devices()
    for i, device in enumerate(devices):
        name = device.lower()
        if ("usb" in name or "fifine" in name) and "monitor" not in name:
            print(f"Found Microphone at Index {i}: {device}")
            return i
    return 3 # Your confirmed Fifine index

def listen_wake_word():
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None
    mic_idx = find_mic_index()

    try:
        # Initialize Porcupine (Requires 16000Hz)
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        
        # Initialize Recorder
        recorder = PvRecorder(device_index=mic_idx, frame_length=porcupine.frame_length)
        
        # PRO-TIP: Check the sample rate if it crashes here
        print(f"Using Sample Rate: {recorder.sample_rate}Hz") 
        
        recorder.start()
        print("Listening for 'Jarvis'...")

        while True:
            pcm = recorder.read()
            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")
                return True

    except Exception as e:
        print(f"Wake Word Error: {e}")
        return False
    finally:
        if recorder:
            recorder.stop()
            recorder.delete()
        if porcupine:
            porcupine.delete()
