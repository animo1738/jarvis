import os, sys, time

# SILENCE ALSA ERRORS: This MUST be the first thing in your file
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

from wake_word import listen_wake_word
from listen import listen_command
from speech import speak
from commands import handle_command
from pvrecorder import PvRecorder

def find_mic():
    """Finds the Fifine mic once at startup."""
    devices = PvRecorder.get_available_devices()
    for i, name in enumerate(devices):
        if "usb" in name.lower() or "fifine" in name.lower():
            return i
    return 1 # Fallback to Index 1

if __name__ == "__main__":
    MIC_INDEX = find_mic()
    print(f"--- Jarvis Started (Mic Index: {MIC_INDEX}) ---")

    while True:
        print("Status: Waiting for 'Jarvis'...")
        
        # 1. Start Wake Word Detection
        if listen_wake_word(MIC_INDEX):
            print("Event: Wake word detected!")
            speak("Yes?")
            
            # 2. Briefly wait for speaker to finish before opening mic for command
            time.sleep(0.3)
            
            # 3. Start Command Recognition
            command = listen_command(MIC_INDEX)
            
            if command:
                print(f"You said: {command}")
                handle_command(command)
            else:
                print("Status: No command heard.")
