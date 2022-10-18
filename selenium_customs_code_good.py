from distutils.spawn import find_executable
from tkinter import Button
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.tariffnumber.com/login") 
time.sleep(2)

elem = driver.find_element(By.ID, "email")  
elem.send_keys("fyenne@hotmail.com")
elem = driver.find_element(By.ID, "password")  
elem.send_keys("assassin")
elem.send_keys(Keys.ENTER)
# driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
driver.get("https://www.tariffnumber.com/services/download") 

driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-link').click()
time.sleep(12)
driver.close()