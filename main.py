import os, sys, time
# Silence ALSA noise
sys.stderr = open(os.devnull, 'w')

from wake_word import listen_wake_word
from listen import listen_command
from speech import speak
from commands import handle_command

if __name__ == "__main__":
    print("--- Jarvis is Active (Using PulseAudio) ---")
    
    while True:
        print("Waiting for 'Jarvis'...")
        # Use index -1 to tell PulseAudio to use the System Default Mic
        if listen_wake_word(device_index=-1):
            print("Wake word detected!")
            speak("Yes?")
            
            # Give the audio server a moment to switch
            time.sleep(0.2)
            
            command = listen_command()
            if command:
                print(f"User: {command}")
                handle_command(command)
