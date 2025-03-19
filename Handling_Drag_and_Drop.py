from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)
time.sleep(2)
actions = ActionChains(browser)
source_element = browser.find_element(By.ID, "column-a")
destination_element = browser.find_element(By.ID, "column-b")

actions.drag_and_drop(source_element,destination_element).perform()
time.sleep(3)