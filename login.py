import time
from selenium import webdriver
from selenium.webdriver.common.by import By

username = "standard_user"
password = "secret_sauce"


driver = webdriver.Chrome()
driver.maximize_window()


login_url = "https://www.saucedemo.com/"
driver.get(login_url)
time.sleep(2)
username_field = driver.find_element(By.ID, value= "user-name")
password_field = driver.find_element(By.ID, value= "password")



username_field.send_keys(username)
password_field.send_keys(password)
time.sleep(2)

login_button = driver.find_element(By.ID, value= "login-button")
assert not login_button.get_attribute("disabled")
login_button.click()
time.sleep(2)

success_element= driver.find_element(By.CSS_SELECTOR, value= ".title")
assert success_element.text == "Products"

time.sleep(5)