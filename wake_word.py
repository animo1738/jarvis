import pvporcupine
#on device wake word detection module like siri
import pyaudio
#audio input output library
import struct


#enables the jarvis to be constantly listening for wakeword
def listen_wake_word():
    porcupine = pvporcupine.create(keywords=["jarvis"])
    #keywords to listen for 
    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
        #input stream details for processing
    )

    print("Waiting for wake word...")

    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        #converts the data to 16 bit signed integers
        if porcupine.process(pcm) >= 0:
            #compares what was heard to the wake words
            return
        
    #constant state of listening 

