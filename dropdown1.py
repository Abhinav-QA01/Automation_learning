import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
login_url = "https://the-internet.herokuapp.com/dropdown"

driver.get(login_url)
driver.maximize_window()

time.sleep(2)

dropdown_element = driver.find_element(By.ID, value = "dropdown")
select = Select(dropdown_element)

# select.select_by_visible_text("Option 2")
# time.sleep(2)

# select.select_by_index(2)
# time.sleep(2)

# select.select_by_value("2")
# time.sleep(2)

'''option_count = len(select.options)
expected_count = 3

if option_count == expected_count:
    print("Test Case passed. Count is correct")
else:
    print("Test case failed. The count is not correct")'''

target_value = "Option 2"

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected Option is {target_value}")
        break
    else:
        print(f"Option {target_value} not found")