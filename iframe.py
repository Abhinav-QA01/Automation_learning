from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.maximize_window()
time.sleep(1)
browser.get('https://the-internet.herokuapp.com/iframe')
time.sleep(2)

iframe = browser.find_element(By.ID, value = "mce_0_ifr")
browser.switch_to.frame(iframe)
time.sleep(2)
Text_Editor = browser.find_element(By.ID, value= 'tinymce')

Text_Editor.clear()
Text_Editor.send_keys("This is selenium with python")
time.sleep(5)

browser.switch_to.default_content()
time.sleep(1)
