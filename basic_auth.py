from selenium import webdriver
import time

user = "admin"
password = "admin"

browser = webdriver.Chrome()
browser.maximize_window()
time.sleep(2)
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
browser.get(url)
time.sleep(3)

