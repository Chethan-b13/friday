import sys
from web_scarper import *
import speech_recognition as sr
from Text_to_speech import *
import os


text: str = ''


def listens():
    global text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            text = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            speak("bro its Time to change you're microphone")
            listens()
        except sr.RequestError:
            speak("Get a wifi router bro")
            listens()
        except:
            speak("try again!")
            listens()


def runner():
    while 1:
        print("listening..!")
        listens()
        print(text)
        if 'news' in text:
            speak("hey chets I'm friday , your personal assistant. Today's headlines")
            get_news()

        elif 'weather' in text or 'climate' in text:
            weather_report()

        elif 'good morning' in text:
            speak("Good morning chets")

        elif 'sleep' in text or 'shutdown' in text or 'exit' in text:
            speak('bye-bye')
            break

        else:
            speak("I didn't get that dude")


def authenticate():
    warning = ['Sorry ,try Again', 'i think, you are not my boss', 'Unauthorized User, Shutting down']
    chance = 0
    while 1:
        if chance > 2:
            sys.exit()
        print("listening....!")
        listens()
        print(text)
        if 'friday' in text:
            speak("hi chets i don't now what time it is,maybe, good afternoon. what can i do for u")
            break
        else:
            speak(warning[chance])
            chance += 1
    runner()


if __name__ == '__main__':
    authenticate()
    os.remove('news.txt')
