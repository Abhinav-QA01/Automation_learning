from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://the-internet.herokuapp.com/horizontal_slider'
browser.get(url)
time.sleep(3)
slider = browser.find_element(By.XPATH, "//input[@type='range']")
actions = ActionChains(browser)
actions.click_and_hold(slider).move_by_offset(15,0).release().perform()
time.sleep(2)
