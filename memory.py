import json
import os
from datetime import datetime, timedelta

MEMORY_FILE = "memory.json"
ARCHIVE_FOLDER = "memory_archives"
ARCHIVE_AGE_DAYS = 30  
# messages older than this get archived

# Ensure files exist
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"history": []}, f, indent=2)

if not os.path.exists(ARCHIVE_FOLDER):
    os.makedirs(ARCHIVE_FOLDER)
    #creates archive folder to store month old messages

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)["history"]

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"history": history}, f, indent=2)

def add_to_memory(user, assistant):
    """Add a new user-assistant pair with timestamp."""
    history = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        "timestamp": timestamp,
        "user": user,
        "assistant": assistant
    })
    save_memory(history)
    archive_old_messages() 
     # check for old messages every time

def archive_old_messages():
    """Move messages older than ARCHIVE_AGE_DAYS to a monthly txt archive."""
    history = load_memory()
    cutoff_date = datetime.now() - timedelta(days=ARCHIVE_AGE_DAYS)
    to_archive = [m for m in history if datetime.strptime(m["timestamp"], "%Y-%m-%d %H:%M:%S") < cutoff_date]
    if not to_archive:
        return  # nothing to archive

    # Create archive file based on month
    month_str = datetime.now().strftime("%Y-%m")
    archive_file = os.path.join(ARCHIVE_FOLDER, f"{month_str}_archive.txt")

    with open(archive_file, "a") as f:
        for m in to_archive:
            f.write(f"[{m['timestamp']}] User: {m['user']}\n")
            f.write(f"[{m['timestamp']}] Jarvis: {m['assistant']}\n\n")

    # Keep only recent messages in memory.json
    recent_history = [m for m in history if datetime.strptime(m["timestamp"], "%Y-%m-%d %H:%M:%S") >= cutoff_date]
    save_memory(recent_history)

def print_memory(limit=10):
    """Helper: print last N conversations."""
    history = load_memory()
    for entry in history[-limit:]:
        print(f"[{entry['timestamp']}] User: {entry['user']}")
        print(f"[{entry['timestamp']}] Jarvis: {entry['assistant']}\n")

