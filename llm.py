import subprocess
from memory import load_memory, add_to_memory

SYSTEM_PROMPT = "You are Jarvis, a concise American AI assistant. Be clear, calm, professional. The current time is {{ now() }}. Keep your responses short and focused on the user's intent."

def ask_llm(user_input):
    memory = load_memory()
    context = SYSTEM_PROMPT + "\n"
    
    for m in memory:
        context += f"User: {m['user']}\nAssistant: {m['assistant']}\n"
    context += f"User: {user_input}\nAssistant:"

    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=context, capture_output=True, text=True
    )

    response = result.stdout.strip()
    add_to_memory(user_input, response)
    return response
