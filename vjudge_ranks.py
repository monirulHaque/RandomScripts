import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'openpyxl'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'maskpass'])

import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import maskpass  # to hide the password
from os import path


# Initializing chrome driver in selenium bot
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

#Navigating to Advising Area
driver.get("https://vjudge.net/contest/543565#rank")
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link.login"))
    )
except:
    print("ERROR: LOGIN BUTTON NOT FOUND!")
login_button.click()
time.sleep(1)
username_input = driver.find_element(By.ID, "login-username")
password_input = driver.find_element(By.ID, "login-password")
username_input.send_keys("monirultanvir63@gmail.com")
pwd = maskpass.advpass()
password_input.send_keys(pwd)
login_button = driver.find_element(By.ID, "btn-login")
login_button.click()

# Waiting for the page to load
try:
    table_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='contest-rank-table']/tbody/tr"))
    )
except:
    print("ERROR: CONTEST TABLE NOT FOUND!")

# Creating the sheet
filename = "contest.xlsx"
wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = "UserName"
ws['B1'] = "Profile URL"
ws['C1'] = "Solved"


# Getting the values
table_rows = driver.find_elements(By.XPATH, "//*[@id='contest-rank-table']/tbody/tr")
row_no = 2
for row in table_rows:
    profile_url = row.find_element(By.CSS_SELECTOR, "a")
    score = row.find_element(By.CLASS_NAME, "solved").text
    ws[f'A{row_no}'] = profile_url.text
    ws[f'B{row_no}'] = profile_url.get_attribute('href')
    ws[f'C{row_no}'] = score
    row_no += 1
    
wb.save(filename)
