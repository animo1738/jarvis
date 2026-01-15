import os
import sys
import time
from wake_word import listen_wake_word
from listen import listen_command 
from speech import speak

# SILENCE ALSA NOISE
sys.stderr = open(os.devnull, 'w')

def main():
    # Use -1 or "default". This tells the libraries: 
    # "Don't look for hardware, just ask PulseAudio for the sound."
    PULSE_INDEX = 1
    
    print("--- Jarvis is now using PulseAudio ---")
    
    while True:
        # 1. Wake word listens to PulseAudio
        if listen_wake_word(PULSE_INDEX):
            print("[Event] Wake word detected.")
            speak("Yes?")
            
            # 2. Command recognition listens to PulseAudio
            # No hardware conflict because PulseAudio shares the stream
            command = listen_command(PULSE_INDEX)
            
            if command:
                print(f"User: {command}")
                # handle_command(command)
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
