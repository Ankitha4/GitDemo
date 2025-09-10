import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon.in']").send_keys("iphone")
driver.find_element(By.XPATH,"input[@name='UserFirstName']").send_keys("Ank")
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(5)

print("new changes1")
print("new changes2")

print("new changes3")