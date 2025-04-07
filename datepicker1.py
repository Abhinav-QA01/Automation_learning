from datetime import datetime,timedelta

from selenium import  webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)
browser.maximize_window()

time.sleep(2)
framelo = browser.find_element(By.XPATH, '//*[@id="post-2661"]/div[2]/div/div/div[1]/p/iframe')
browser.switch_to.frame(framelo) 
time.sleep(3)
browser.find_element(By.XPATH, "//input[@id='datepicker']").click()

current_date = datetime.now()
next_date = current_date + timedelta(days=0)
formatted_date = next_date.strftime("%m/%d/%y")
browser.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys(formatted_date + Keys.TAB)
time.sleep(3)