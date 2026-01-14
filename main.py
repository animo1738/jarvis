import time
from wake_word import listen_wake_word
from listen import listen
from speech import speak
from commands import handle_command
from reminders import today_events, upcoming_within_hour
from datetime import datetime

ACTIVE_TIMEOUT = 20

print("Jarvis started")


# Daily agenda announcement
events = today_events()
if events:
    speak("Good morning. Today's agenda:")
    for e in events:
        speak(f"{e['time']} {e['text']}")
MIC_INDEX = 2 
while True:
    print("Waiting for wake word...")
    if listen_wake_word(mic_index=MIC_INDEX):
    
    # ADD THIS: Give the hardware 0.5 seconds to breathe
    time.sleep(0.5) 
    
    print("Wake word detected")
    speak("Yes?")

    start = time.time()

    while time.time() - start < ACTIVE_TIMEOUT:

        # Check for reminders
        alerts = upcoming_within_hour()
        now_time = datetime.now().strftime("%H:%M")
        for e in alerts:
            if e["time"] == now_time:
                speak(f"Reminder: {e['text']}")

        # Listen to command
        command = listen(mic_index=MIC_INDEX)
        if command:
            state = handle_command(command)
            if state == "sleep":
                break
            start = time.time()

        time.sleep(1)

    speak("Sleeping")
