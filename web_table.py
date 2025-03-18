from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Initialize WebDriver
driver = webdriver.Chrome()  # Use appropriate WebDriver

# Open the webpage
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
time.sleep(3)

driver.execute_script("window.scrollTo(0,700)")
time.sleep(2)

# Find the total number of rows
rows = len(driver.find_elements(By.XPATH, '//*[@id="countries"]/tbody/tr'))

# Loop through each row and check the checkbox
for n in range(2, rows + 1):  # Assuming row index starts from 1
    checkbox_xpath = f'//*[@id="countries"]/tbody/tr[{n}]/td[1]/input'
    checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    
    # Check the checkbox only if it's not already selected
    if not checkbox.is_selected():
        checkbox.click()
time.sleep(3)
print("All checkboxes are checked successfully!")
