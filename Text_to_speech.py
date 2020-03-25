import pyttsx3

engine = pyttsx3.init()



def speak(message='hello world'):
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice)
    engine.setProperty('voice', voices[24].id)
    engine.say(message)
    engine.runAndWait()


def stops():
    engine.stop()
