import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'openpyxl'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'maskpass'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'webdriver-manager'])

import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import maskpass  # to hide the password
from os import path


# Initializing chrome driver in selenium bot
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

#Navigating to the form
driver.get("https://docs.google.com/forms/d/1Kpb7YGmDctrvLsPG2SpMbCYyujKayswIDF0VX7TKWRA/edit")
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierNext"))
    )
except:
    print("ERROR: LOGIN BUTTON NOT FOUND!")

time.sleep(1)
username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys("ext.monirul.haque@bracu.ac.bd")
login_button.click()
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwordNext"))
    )
except:
    print("ERROR: LOGIN BUTTON NOT FOUND!")
time.sleep(1)
password_input = driver.find_element(By.NAME, "Passwd")
pwd = ""
# pwd = maskpass.advpass()
password_input.send_keys(pwd)
login_button.click()

total_sets = 2

time.sleep(3)
edit_button = driver.find_element(By.CLASS_NAME, u"HMRMj")
driver.implicitly_wait(1)
ActionChains(driver).move_to_element(edit_button).click(edit_button).perform()

time.sleep(3)
driver.implicitly_wait(1)
division = driver.find_element(By.CLASS_NAME, u"ibnC6b-LpPrec-byTLUb")
driver.execute_script("arguments[0].click();", division)


time.sleep(3)
lst = driver.find_elements(By.CLASS_NAME, u"jgvuAb")

a = 0
c = 2
try:
    for entry in lst:
        clickable_elem = entry.find_element(By.CLASS_NAME, u"ry3kXd")
        print(entry)
        print(dir(entry))
        print(entry.id,'-------------------------------------')
        # print(entry.id)
        time.sleep(0.5)
        if a == 0 or a == len(lst)-1:
            a += 1
            continue
        
        driver.execute_script("arguments[0].click();", clickable_elem)
        time.sleep(1)
        print('ye1')
        lst2 = driver.find_elements(By.CLASS_NAME, u"jgvuAb")
        entry2 = lst2[a]
        print(entry2.id,'-------------------------------------')
        time.sleep(0.5)
        div = entry2.find_element(By.CLASS_NAME, "ncFHed")
        print('ye2')
        options = div.find_elements(By.CLASS_NAME, "MocG8c")

        b = 0
        if c-2>=total_sets:
            print('yessssssssssssssssssssss')
            c = 2
        print('-------------------',c)
        for opt in options:
            if b==c:
                # driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", opt, "tabindex", "0")
                print('hehe1')
                span = opt.find_element(By.TAG_NAME, "span")
                driver.execute_script("arguments[0].click();", span)
                time.sleep(0.5)
            b += 1
        if a%5 == 0:
            driver.execute_script("window.scrollTo(0, 1000)")
            time.sleep(0.5)
        a += 1
        c += 1
        
            

except:
    time.sleep(500)
# //div[contains(@class,'Ed9blf')]//div[3]//div[1]//div[3]//div[6]//div[1]//div[1]//div[1]//div[1]//div[3]//span[1]
# //div[contains(@class,'OA0qNb ncFHed QXL7Te qs41qe')]//span[contains(@class,'vRMGwf oJeWuf')][normalize-space()='Continue to next section']
# // jgvuAb ybOdnf dB1UHb llrsB
# body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > span:nth-child(2)
