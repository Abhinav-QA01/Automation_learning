from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://selenium.dev")
driver.maximize_window()
time.sleep(10)
