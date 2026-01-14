import pvporcupine
from pvrecorder import PvRecorder

def listen_wake_word(mic_idx):
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        recorder = PvRecorder(device_index=mic_idx, frame_length=porcupine.frame_length)
        
        recorder.start()
        
        while True:
            pcm = recorder.read()
            if porcupine.process(pcm) >= 0:
                return True # Exit and trigger the 'finally' block to release mic

    except Exception as e:
        # If we catch an error, print it to the real stderr so you see it
        sys.__stderr__.write(f"Wake Word Hardware Error: {e}\n")
        return False
    finally:
        # IMPORTANT: This releases the hardware so listen.py can use it
        if recorder is not None:
            recorder.stop()
            recorder.delete()
        if porcupine is not None:
            porcupine.delete()
