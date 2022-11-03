from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import base64
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://cyberark.eu.dir.bunge.com/PasswordVault/v10/Accounts")
time.sleep(2)
WebDriverWait(driver, 600).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.auth-select__auth_icon'))
    ) 
driver.find_elements(By.CSS_SELECTOR, 'div.auth-select__auth_icon')[1].click() # 点击中间那个图标.
# ---------------------------------------------------------------------------- #
#                              login successfullyX                             #
# ---------------------------------------------------------------------------- #
time.sleep(5)
try:
    find_email_input_box = driver.find_element(By.CSS_SELECTOR, 'input#i0116')
except:
    find_email_input_box = None
if find_email_input_box:
    find_email_input_box.clear()
    find_email_input_box.send_keys('samo.yan@bunge.com')
    find_email_input_box.send_keys(Keys.ENTER)
    time.sleep(2)
    find_psswd_input_box = driver.find_element(By.CSS_SELECTOR, 'input#i0118')
    if find_psswd_input_box:
        print(1)
        find_psswd_input_box.clear()
        a = b'QUlnb25nenVvNz0='
        a = base64.standard_b64decode(a).decode("utf-8") 
        find_psswd_input_box.send_keys(a)
        find_psswd_input_box.send_keys(Keys.ENTER)
    # driver.s
else:
    print('no need to input pass code')

WebDriverWait(driver, 400).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id='frame-epv']"))
    )
time.sleep(5)
driver.switch_to.frame("frame-epv")
print('switch')
WebDriverWait(driver, 400).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label^='mor']"))
    )
driver.find_element(By.CSS_SELECTOR, "button[aria-label^='mor']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "div[class^='action-menu-item'][data-testid='action-menu-item-2']").click()
print('===finished===\n')
# WebDriverWait(driver, 400).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "div[class^='feedback__content__']"))
#     )
 
time.sleep(5)
# read clipboard?
d = pd.read_clipboard(header = None)
d['timestamp'] = datetime.today().strftime('%Y%m%d')
print(d)
route = r"D:\samo\app1_dashboard\datadown\cred.txt"
# route = r"C:\Users\SRV-USAMYAN\Documents\My SugarSync\app1_dashboard\datadown\cred.txt"
d.to_csv(route, index = None)
driver.close()
