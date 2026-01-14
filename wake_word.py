import pvporcupine
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


def listen_wake_word(mic_index=2): # Set your default index here
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None
    mic_idx = find_mic_index()
    if mic_idx is None:
        print("Warning: Auto-search failed. Falling back to Index 3.")
        mic_idx = 3
    try:
        # Initialize Porcupine
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        
        # Initialize Recorder with the specific mic index
        recorder = PvRecorder(device_index=mic_idx, frame_length=porcupine.frame_length)
        recorder.start()

        while True:
            pcm = recorder.read()
            if porcupine.process(pcm) >= 0:
                return True # Wake word detected!

    except Exception as e:
        print(f"Wake Word Error: {e}")
        return False
    finally:
        # CLEANUP: This is the most important part to prevent Segfaults
        if recorder:
            recorder.stop()
            recorder.delete()
        if porcupine:
            porcupine.delete()
