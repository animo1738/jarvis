from speech import speak
from reminders import add_event, today_events
from lists import add_to_category
from llm import ask_llm
import datetime
import json

def handle_command(cmd):
    cmd_lower = cmd.lower()

    if "good morning" in cmd_lower:
        from morning import give_morning_brief
        gave_brief = give_morning_brief()
        if not gave_brief:
            speak("You already received your morning brief today.")
        return "active"

    elif "sleep" in cmd_lower:
        speak("Going to sleep for now")
        return "sleep"

    elif "time" in cmd_lower:
        speak(datetime.datetime.now().strftime("%H:%M"))
        return "active"

    elif "agenda" in cmd_lower or "schedule" in cmd_lower:
        events = today_events()
        if not events:
            speak("You have nothing planned today")
        else:
            speak("Today's agenda:")
            for e in events:
                speak(f"{e['time']} {e['text']}")
        return "active"
    

    else:
        response = ask_llm(f"""
        You are Jarvis, a helpful assistant.
        Interpret the user's command below. 
        If the user wants to add an event, respond ONLY in this JSON format:
        {{ "action": "add_event", "day": "day_of_week", "time": "HH:MM", "text": "description" }}
        If the user wants to something to a list, respond ONLY in this JSON format:
        {{{ "action": "add_to_list", "category": "category_name", "item": "item_text" }}}                   
                           
        If it is a general query or chat, respond normally in plain text.
        User command: "{cmd}"
        """)
        
        try:
            parsed = json.loads(response)
            if parsed.get("action") == "add_event":
                add_event(parsed["day"], parsed["time"], parsed["text"])
                speak(f"Event '{parsed['text']}' added for {parsed['day']} at {parsed['time']}")
            elif parsed.get("action") == "add_to_list":
                category = parsed["category"]
                item = parsed["item"]

                add_to_category(category, item)
                speak(f"Added {item} to {category}")

            else:
                speak(response)
        except json.JSONDecodeError:
                speak(response)

    return "active"
