import time
from pvrecorder import PvRecorder
from wake_word import listen_wake_word
from listen import listen
from speech import speak
from commands import handle_command
from reminders import today_events, upcoming_within_hour
from datetime import datetime

ACTIVE_TIMEOUT = 20

print("Jarvis started")

def find_mic_index():
    devices = PvRecorder.get_available_devices()
    for i, device in enumerate(devices):
        name = device.lower()
        if ("usb" in name or "fifine" in name) and "monitor" not in name:
            print(f"Found Microphone at Index {i}: {device}")
            return i
    for i, device in enumerate(devices):
        if "monitor" not in device.lower():
            return i
    return None
# Daily agenda announcement
events = today_events()
if events:
    speak("Good morning. Today's agenda:")
    for e in events:
        speak(f"{e['time']} {e['text']}")


MIC_INDEX = find_mic_index()
while True:
    print("Waiting for wake word...")
    if listen_wake_word(mic_index=MIC_INDEX):
        
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

            time.sleep(0.1)

        speak("Sleeping")
