#!/usr/bin/python3


#pip3 install pyttsx3 SpeechRecognition pyaudio


import random
import datetime
#import webbrowser
import pyttsx3
#import wikipedia
#from pygame import mixer
import speech_recognition as sr
#from speech_recognition.__main__ import r, audio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

#engine.setProperty('rate', rate - 25)

engine.say('I didnt get that. Rerun the code')
engine.runAndWait()


while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')

            engine.runAndWait()

