import pvporcupine
from pvrecorder import PvRecorder

def listen_wake_word(device_index=-1):
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        # device_index=-1 picks the PulseAudio default input
        recorder = PvRecorder(device_index=device_index, frame_length=porcupine.frame_length)
        recorder.start()

        while True:
            pcm = recorder.read()
            if porcupine.process(pcm) >= 0:
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
