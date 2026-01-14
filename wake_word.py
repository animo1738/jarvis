import pvporcupine
#on device wake word detection module like siri
import pyaudio
#audio input output library
import struct


#enables the jarvis to be constantly listening for wakeword
def listen_wake_word():
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    pa = pyaudio.PyAudio()
    
    # Force it to use the Fifine Mic found at Index 2
    mic_index = 2 

    try:
        # Use 'porcupine' for testing as it's the most stable default keyword
        porcupine = pvporcupine.create(access_key=access_key, keywords=["porcupine"])
        
        stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            input_device_index=mic_index, # <--- THIS FIXES THE SEGFAULT
            frames_per_buffer=porcupine.frame_length
        )

        print("Jarvis is active. (Say 'Porcupine' to test)")

        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")
                return # Exit back to main.py to handle the command
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Proper cleanup stops the audio hardware from 'hanging'
        pa.terminate()
