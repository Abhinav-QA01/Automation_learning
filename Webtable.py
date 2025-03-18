from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()
time.sleep(3)

browser.execute_script("window.scrollTo(0,700)")

table = browser.find_element(By.ID, value="countries")
rows = table.find_elements(By.TAG_NAME,value = "tr")
row_count = len(rows)
print(row_count)
target_value = "India"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, value="td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found the {target_value}")
            found = True
            break
    if found:
        break 
if not found:
    print(f"Target value{target_value} not found")

for row in rows:
    cell = row.find_elements(By.TAG_NAME, value="td")
    for cell in cells:
        checkbox1 = cell.find_element(By.XPATH, value= '//*[@id="countries"]/tbody/tr[2]/td[1]/input').click()
        checkbox2 = cell.find_element(By.XPATH, value = '//*[@id="countries"]/tbody/tr[3]/td[1]/input').click()

time.sleep(2)
