from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://selenium.dev/")
driver.maximize_window()

title = driver.title
print(title)
assert "Selenium" in title

driver.find_element(By.PARTIAL_LINK_TEXT(""))
