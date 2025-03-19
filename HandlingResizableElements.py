from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time

browser = webdriver.Chrome()

url = 'https://demo.automationtesting.in/Resizable.html'
browser.get(url)

browser.maximize_window()
time.sleep(3)
resizable_element = browser.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
Initial_elemnt_size = browser.find_element(By.XPATH, '//*[@id="resizable"]')
initial_size = Initial_elemnt_size.size
print("Initial size: ", initial_size)
time.sleep(2)
action_chains = ActionChains(browser)
action_chains.click_and_hold(resizable_element).move_by_offset(100, 100).release().perform()

time.sleep(3)

resized_element = Initial_elemnt_size.size
print("Resized Element: ", resized_element)
time.sleep(3)