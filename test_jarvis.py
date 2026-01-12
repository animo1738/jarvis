from speech import speak
from commands import handle_command
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

speak("Jarvis speech test starting. Say 'stop' to quit.")

while True:
    with mic as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio)
        print(f"You said: {cmd}")
        if cmd.lower() == "stop":
            speak("Stopping Jarvis test.")
            break
        handle_command(cmd)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Speech recognition service unavailable.")
