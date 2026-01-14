import pvporcupine
from pvrecorder import PvRecorder

def listen_wake_word():
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    
    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])
        
        # We use index 2 (Fifine Mic) from your scan
        recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
        recorder.start()

        print("Jarvis is listening... (Say 'Jarvis')")

        while True:
            pcm = recorder.read()
            result = porcupine.process(pcm)
            if result >= 0:
                print("Wake word detected!")
                
                break
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Proper cleanup is much easier here
        if 'recorder' in locals():
            recorder.stop()
            recorder.delete()
        if 'porcupine' in locals():
            porcupine.delete()
