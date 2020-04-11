#!/usr/bin/env python3

#pip3 install selenium pyautogui

import pyautogui
from selenium import webdriver
profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0")
profile.update_preferences()
browser = webdriver.Firefox(firefox_profile=profile,executable_path = '/usr/local/bin/geckodriver')
browser.get("http://localhost/chatbot")
pyautogui.press('f11')

