from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(3)
# Switching to top frame
browser.switch_to.frame("frame-top")

# Switching to middle frame
browser.switch_to.frame("frame-middle")

content = browser.find_element(By.ID,"content").text
print("Content in middle frame", content)
time.sleep(3)

# Switch to default content
browser.switch_to.default_content()

# Switching to bottom frame
browser.switch_to.frame("frame-bottom")


content_Bottom = browser.find_element(By.TAG_NAME,"body").text
print("Content in bottom frame", content_Bottom)
time.sleep(2)
