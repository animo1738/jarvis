import time
from wake_word import listen_wake_word
from listen import listen
from speech import speak
from commands import handle_command

print("Jarvis started")

# (Your find_mic_index logic was here too)

while True:
    print("Waiting for wake word...")
    if listen_wake_word():
        time.sleep(0.5) 
        print("Wake word detected")
        speak("Yes?")
    
        start = time.time()
        while time.time() - start < 20: # ACTIVE_TIMEOUT
            command = listen()
            if command:
                state = handle_command(command)
                if state == "sleep":
                    break
                start = time.time()
            time.sleep(0.1)
        speak("Sleeping")
