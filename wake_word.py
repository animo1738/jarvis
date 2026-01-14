import pvporcupine
from pvrecorder import PvRecorder

def listen_wake_word(mic_index=2): # Set your default index here
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None

    try:
        # Initialize Porcupine
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        
        # Initialize Recorder with the specific mic index
        recorder = PvRecorder(device_index=mic_index, frame_length=porcupine.frame_length)
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
