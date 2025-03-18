import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
browser.maximize_window()

time.sleep(2)

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# browser.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()

time.sleep(1)
checkboxes = browser.find_elements(By.XPATH, value = "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

time.sleep(2)
checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_checked_count = 7  
if checked_count == expected_checked_count:
    print('Checkbox count is verified')

else:
    print("Checkbox count is mismatched")

time.sleep(3)