from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

actions = ActionChains(browser)
hover_element = browser.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
actions.move_to_element(hover_element).perform()
time.sleep(3)

browser.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(2)

