import pyttsx3
#uses linux built in text to speech engine to produce spoken audio, basis of our jarvis talking back to us

engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()
