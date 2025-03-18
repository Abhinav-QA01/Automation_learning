import time
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
browser.switch_to.new_window()
browser.get("https://playwright.dev/")
time.sleep(2)

number_of_tabs= len(browser.window_handles)
print(number_of_tabs)
tabs_value = browser.window_handles
print(tabs_value)

current_tab = browser.current_window_handle
print(current_tab)

browser.find_element(By.CSS_SELECTOR, value = ".getStarted_Sjon").click()
FirstTab = browser.window_handles[0]

if current_tab != FirstTab:
    browser.switch_to.window(FirstTab)
time.sleep(2)
browser.find_element(By.XPATH, value = "//span[normalize-space()='Downloads']").click()
time.sleep(2)
