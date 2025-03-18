from selenium import webdriver

import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

browser.maximize_window()
time.sleep(2)
AlertButton = browser.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
AlertButton.click()
time.sleep(2)
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(3)

alert.dismiss()
time.sleep(3)

AlertButton = browser.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
AlertButton.click()
time.sleep(2)
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)

alert.send_keys("This is selenium tutorial")

alert.accept()
time.sleep(3)