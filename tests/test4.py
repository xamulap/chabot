#!/usr/bin/python3

#pip install py-espeak-ng espeak-ng

from espeakng import ESpeakNG

esng = ESpeakNG()
esng.voice = "english"
esng.say("Hello World!")

esng.voice = "slovak" 
esng.say("Test 123")
#esng.say("Hallo Welt!")

