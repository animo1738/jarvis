import pvporcupine
import pvrecorder
from pvrecorder import PvRecorder

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

def listen_wake_word():
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None
    mic_idx = find_mic_index()

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        
        # We wrap the recorder startup in its own check
        recorder = PvRecorder(device_index=mic_idx, frame_length=porcupine.frame_length)
        
        print(f"Attempting to start recording at {porcupine.sample_rate}Hz...")
        recorder.start()
        print("Listening for 'Jarvis'...")

        while True:
            pcm = recorder.read()
            if porcupine.process(pcm) >= 0:
                return True

    except Exception as e:
        print(f"Wake Word Error: {e}")
        return False
    finally:
        # Check if they exist BEFORE calling methods on them
        if recorder is not None:
            try:
                recorder.stop()
                recorder.delete()
            except:
                pass
        if porcupine is not None:
            porcupine.delete()
