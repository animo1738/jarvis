import json
import datetime

FILE = "agenda.json"

def load():
    with open(FILE, "r") as f:
        return json.load(f)["events"]
    #opens the events file and its components

def save(events):
    with open(FILE, "w") as f:
        json.dump({"events": events}, f, indent=2)
        #saves all events made 

def add_event(day, time, text):
    events = load()
    events.append({"day": day, "time": time, "text": text})
    save(events)
    #appends events to the files in the specific format to calendarise it

def upcoming_within_hour():
    now = datetime.datetime.now()
    today = now.strftime("%A").lower()
    alerts = []

    for e in load():
        if e["day"] == today:
            event_time = datetime.datetime.strptime(e["time"], "%H:%M").replace(
                year=now.year, month=now.month, day=now.day
            )
            delta = (event_time - now).total_seconds() / 60
            if 0 < delta <= 60:
                alerts.append(e)

    return alerts
    # returns all events in the upcoming hour and labels them as alerts


