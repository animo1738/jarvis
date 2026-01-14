import pvporcupine
#on device wake word detection module like siri
import pyaudio
#audio input output library
import struct


#enables the jarvis to be constantly listening for wakeword
def listen_wake_word():
    access_key = "9ta+47WGMP6Wb0szstPJ2D/0cZ8L5ev2wUjrcV3aBn+hzK33pZ6WYw=="
    pa = pyaudio.PyAudio()
    
    #
    mic_index = 2 

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["porcupine"])
        
        stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            input_device_index=mic_index, 
            frames_per_buffer=porcupine.frame_length
        )

        print("Jarvis is active. (Wake word: 'Porcupine')")

        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")
                return
    finally:
        pa.terminate()
