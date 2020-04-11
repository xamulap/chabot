#!/usr/bin/python3


#pip3 install selenium


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


#options = Options()
#options.headless = True

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0")
profile.update_preferences()

driver = webdriver.Firefox()
#driver = webdriver.Firefox(firefox_profile=profile,executable_path = '/usr/local/bin/geckodriver')

driver.get("http://localhost/chatbot")
#driver.manage().window().maximize()
#driver.maximize_window()
driver.find_element_by_xpath('/html/body').send_keys(Keys.F11)
#pyautogui.press('f11')

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

