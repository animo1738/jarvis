import subprocess
from memory import load_memory, add_to_memory
from reminders import upcoming_within_hour

SYSTEM_PROMPT = """
You are Jarvis, a concise American AI assistant.
Be clear, calm, professional.
Do not ramble. Keep sentences short and formal.

"""
# defines how the Assistant acts

def ask_llm(user_input):
    memory = load_memory()
    agenda_alerts = upcoming_within_hour()

    context = SYSTEM_PROMPT + "\n"

    if agenda_alerts:
        context += "Upcoming events within one hour:\n"
        for e in agenda_alerts:
            context += f"- {e['time']} {e['text']}\n"

    for m in memory:
        context += f"User: {m['user']}\nAssistant: {m['assistant']}\n"

    context += f"User: {user_input}\nAssistant:"

    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=context,
        capture_output=True,
        text=True
    )

    response = result.stdout.strip()
    add_to_memory(user_input, response)
    return response
