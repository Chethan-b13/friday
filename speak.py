import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Boss")
engine.setProperty('rate', 100)
print(engine.getProperty('voices'))
engine.runAndWait()
