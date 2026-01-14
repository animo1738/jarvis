
---
<p align="center">
  <h1 align="center">Jarvis – Raspberry Pi Personal Assistant </h1>
</p>

<p align="center">
  <b>Jarvis is a lightweight voice‑activated personal assistant designed to run on a Raspberry Pi 4.  
It listens for a wake word, processes speech, interacts with an LLM, manages reminders, stores memory, and delivers a daily morning briefing.</b>
</p>

## Features

- **Wake‑word detection** (`wake_word.py`)
- **Speech recognition** and **text‑to‑speech** (`speech.py`)
- **LLM integration** for conversational responses (`llm.py`)
- **Agenda + reminders system** (`agenda.json`, `reminders.py`)
- **Persistent memory** (`memory.json`, `memory.py`)
- **Morning briefing generator** (`morning.py`)
- **Continuous listening loop** (`listen.py`, `main.py`)

---

## Hardware Requirements

- Raspberry Pi 4 (2GB+ recommended)
- USB microphone or ReSpeaker hat
- Speakers or 3.5mm audio output
- Stable internet connection (for LLM API calls)

---

## Software Requirements

- Python 3.9+  
- Linux (Raspberry Pi OS recommended)

---
## What's Next

- API and internet connection features (IMDB, weather, prayer times, Spotify, email reading, local news)
- Connection to home assistant and peripherals like LEDs and motion detectors for smart home integration
- Integration with Telegram to send messages
- Local LLM upgrade (Jetson Nano or RPi5
  
---

## Installation

### 1. Update your Pi
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install system dependencies
```bash
sudo apt install python3 python3-pip portaudio19-dev ffmpeg -y
```
### 3. Clone the repository
```bash
git clone https://github.com/animo1738/jarvis
cd jarvis
```

### 4. Install Python dependencies
```bash
pip3 install -r requirements.txt
sudo apt install espeak-ng libespeak1
```

### 5. Running Jarvis
```bash
python3 main.py
```






