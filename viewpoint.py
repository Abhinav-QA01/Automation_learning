import time

from selenium import webdriver
viewports = [(768,1024), (1024,768), (356,2342), (414,896)]
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

# driver.set_window_size(width=768,height=1024)
# time.sleep(4)

try: 
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(3)

finally:
    time.sleep(5)
    driver.close()