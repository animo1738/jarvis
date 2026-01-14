import os
import sys
import time
from wake_word import listen_wake_word
from listen import listen_command 
from speech import speak
from commands import handle_command
from pvrecorder import PvRecorder

# Silence the ALSA/JACK warnings that flood the terminal
sys.stderr = open(os.devnull, 'w')

def get_mic_index():
    from pvrecorder import PvRecorder
    devices = PvRecorder.get_available_devices()
    
    sys.__stderr__.write("--- Searching for Microphone ---\n")
    for i, name in enumerate(devices):
        name_lower = name.lower()
        
        # KEY FIX: Check for 'usb' or 'fifine' AND ensure 'monitor' is NOT in the name
        if ("usb" in name_lower or "fifine" in name_lower) and "monitor" not in name_lower:
            sys.__stderr__.write(f"Selected Device: Index {i} - {name}\n")
            return i
            
    # Fallback: find any device that isn't a monitor if the Fifine isn't found
    for i, name in enumerate(devices):
        if "monitor" not in name.lower():
            return i
            
    return 0

def main():
    mic_idx = get_mic_index()
    print(f"--- Jarvis System Initialized (Mic Index: {mic_idx}) ---")
    
    while True:
        print("\n[Status] Waiting for 'Jarvis'...")
        
        # Step 1: Listen for Wake Word
        if listen_wake_word(mic_idx):
            print("[Event] Wake word detected.")
            speak("Yes?")
            
            # Step 2: Listen for Command
            # We pass the mic index so it doesn't have to search again
            command = listen_command(mic_idx)
            
            if command:
                print(f"[User] {command}")
                # handle_command should return "sleep" to break the active loop
                handle_command(command)
            else:
                print("[Status] No command detected, returning to standby.")
        
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[System] Shutting down Jarvis...")
        sys.exit(0)
