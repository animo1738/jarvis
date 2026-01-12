import json
import os
from datetime import datetime
from reminders import today_events
from speech import speak

BRIEF_FILE = "morning_brief.json"

if not os.path.exists(BRIEF_FILE):
    with open(BRIEF_FILE, "w") as f:
        json.dump({"last_brief_date": ""}, f, indent=2)

def give_morning_brief():
    today_str = datetime.now().strftime("%Y-%m-%d")

    with open(BRIEF_FILE, "r") as f:
        data = json.load(f)

    if data.get("last_brief_date") == today_str:
        return False

    events = today_events()
    if not events:
        speak("Good morning. You have nothing scheduled today.")
    else:
        speak("Good morning. Today's agenda:")
        for e in events:
            speak(f"{e['time']} {e['text']}")

    data["last_brief_date"] = today_str
    with open(BRIEF_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return True
