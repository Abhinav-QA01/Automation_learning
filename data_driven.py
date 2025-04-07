from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

csv_file= 'testdata.csv'
test_data = []
with open(csv_file,'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

print(test_data)
for data in test_data:
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, 'user-name').send_keys(data['ï»¿username'])
    driver.find_element(By.ID, 'password').send_keys(data['password'])
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)

