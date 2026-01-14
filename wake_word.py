import pvporcupine
from pvrecorder import PvRecorder

def listen_wake_word(mic_idx):
    # YOUR ACCESS KEY
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    porcupine = None
    recorder = None

    try:
        # keywords=["jarvis"] uses the built-in Jarvis model
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        recorder = PvRecorder(device_index=mic_idx, frame_length=porcupine.frame_length)
        
        recorder.start()
        
        while True:
            pcm = recorder.read()
            # If keyword is detected, it returns the index (0 in this case)
            if porcupine.process(pcm) >= 0:
                return True

    except Exception as e:
        # Use sys.__stderr__ to print if you need to see real errors while ALSA is silenced
        return False
    finally:
        # This is the most important part for preventing "Device Busy" errors
        if recorder is not None:
            recorder.stop()
            recorder.delete()
        if porcupine is not None:
            porcupine.delete()
