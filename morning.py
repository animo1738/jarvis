import json, os
from datetime import datetime
from reminders import today_events

BRIEF_FILE = "morning_brief.json"

def get_morning_brief_text():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    if os.path.exists(BRIEF_FILE):
        with open(BRIEF_FILE, "r") as f:
            data = json.load(f)
        if data.get("last_brief_date") == today_str:
            return "You have already received your brief today, sir."

    events = today_events()
    if not events:
        msg = "Good morning. Your schedule is clear today."
    else:
        msg = "Good morning. Your agenda includes: " + ". ".join([f"{e['time']} {e['text']}" for e in events])

    with open(BRIEF_FILE, "w") as f:
        json.dump({"last_brief_date": today_str}, f)
    
    return msg
