import datetime
import json
from reminders import add_event, today_events
from llm import ask_llm
from morning import get_morning_brief_text

def handle_command(cmd):
    cmd_lower = cmd.lower()

    if "good morning" in cmd_lower:
        return get_morning_brief_text()

    elif "time" in cmd_lower:
        return f"Sir, the time is {datetime.datetime.now().strftime('%H:%M')}"

    elif "agenda" in cmd_lower or "schedule" in cmd_lower:
        events = today_events()
        if not events:
            return "You have nothing planned today."
        
        brief = "Today's agenda: " + ", ".join([f"{e['time']} {e['text']}" for e in events])
        return brief

    else:
        # Ask your local Ollama instance
        response = ask_llm(cmd)
        
        try:
            parsed = json.loads(response)
            if parsed.get("action") == "add_event":
                add_event(parsed["day"], parsed["time"], parsed["text"])
                return f"Event {parsed['text']} added for {parsed['day']} at {parsed['time']}."
            return response
        except:
            return response
