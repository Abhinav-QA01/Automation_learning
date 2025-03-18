from datetime import datetime,timedelta

from selenium import  webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
browser.maximize_window()
time.sleep(3)

browser.find_element(By.ID, "datepicker2").click()

time.sleep(3)

current_date = datetime.now()

next_day = current_date + timedelta(days=1)
time.sleep(2)
print(next_day)

Next_day = (str(next_day.day))

current_month = datetime.now().month
current_year = datetime.now().year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}"
Month_Dropdown = browser.find_element(By.XPATH, "//select[@title='Change the month']")

select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))
time.sleep(3)
Year_Dropdown = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/select[2]")
select = Select(Year_Dropdown)
time.sleep(3)
select.select_by_visible_text("2025")

browser.find_element(By.LINK_TEXT, Next_day).click()

time.sleep(3)