#!/usr/bin/python3

##install
#pip3 install threaded py-espeak-ng SpeechRecognition pyaudio
#apt install espeak-ng
#download https://github.com/mozilla/geckodriver/releases 


from espeakng import ESpeakNG
import http.server
import socketserver
import pyautogui
from selenium import webdriver
import threading
import time
import speech_recognition as sr

PORT = 8000
debug = True
gecko_path = "/usr/local/bin/geckodriver"

##start http server
Handler = http.server.SimpleHTTPRequestHandler
server_address = ('127.0.0.1', PORT)
httpd = socketserver.TCPServer(("", PORT), Handler)
thread = threading.Thread(target=httpd.serve_forever)
thread.start()

##load gui
profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0")
profile.update_preferences()
browser = webdriver.Firefox(firefox_profile=profile,executable_path = gecko_path)
url = "http://localhost:" + str(PORT) + "/html"
browser.get(url)
#for debug no fullscreen
if(not debug):
	pyautogui.press('f11')

##say hella
time.sleep(5)
esng = ESpeakNG()
esng.voice = "slovak"
#speaking move
browser.execute_script("return move();")
esng.say("Ahoj Olívia. Moje meno je Matúš.")
time.sleep(5)
browser.execute_script("return move();")
esng.say("Chceš sa so mnou hrať?")

##listen
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=0.2)
	audio = r.listen(source)
	try:
		print("You said: " + r.recognize_google(audio, language="sk-SK"))
		browser.execute_script("return move();")
		esng.say("Dobre")
	except sr.UnknownValueError:
		print("No audio")



