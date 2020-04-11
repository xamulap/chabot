#!/usr/bin/python3


#pip3 install pyttsx3 SpeechRecognition pyaudio


import speech_recognition as sr
import datetime

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source,5)
        try:
            print("You said:- " + r.recognize_google(audio,language="sk-SK"))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')

            engine.runAndWait()

