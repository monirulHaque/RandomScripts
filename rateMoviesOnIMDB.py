from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import imdb
from imdb import Cinemagoer

# opts = webdriver.ChromeOptions()
#adding specific Chrome Profile Path
# opts.add_argument("--headless")
# opts.add_argument("--no-sandbox")

#provide location where chrome stores profiles
# opts.add_argument(r"--user-data-dir=/home/monirul/.config/google-chrome")

#provide the profile name with which we want to open browser
# opts.add_argument(r'--profile-directory=Profile 1')
# opts.add_arguments = {'user-data-dir':"Profile 1"}

# opts.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# driver = webdriver.Chrome(options=opts)
driver = webdriver.Chrome()

driver.get("https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "signInSubmit"))
    )
except:
    print("ERROR: LOGIN BUTTON NOT FOUND!")
username_input = driver.find_element(By.ID, "ap_email")
password_input = driver.find_element(By.ID, "ap_password")
username_input.send_keys("monirultanvir63@gmail.com")
# pwd = maskpass.advpass()
pwd = ''   
password_input.send_keys(pwd)
# login_button = driver.find_element(By.ID, "signInSubmit")
login_button.click()
time.sleep(25)


ia = Cinemagoer()
'''
txt file format
• Zodiac - 8; After a certain point it feels like they are just prolonging the movie
• Dark City - 7; I liked the mystery but the ending was messed up
• The Menu - 6; The ending was idiotic and the most annoying character survived in the end for some reason
• V for Vendetta - 7; The ending was weird
'''
seenList = open('moviesSeenList.txt')
unratedList = []
while(True):
    temp = seenList.readline()
    if temp == "":
        break
    movieInfo = temp.split(";")
    movieName, rating = movieInfo[0].split("-")
    movieName = movieName.lstrip("• ").rstrip()
    rating = int(rating.strip())
    movies = ia.search_movie(movieName)
    # print(movies)
    print(movies[0].movieID)
    print(movies[0], rating)
    driver.get(f"https://www.imdb.com/title/tt{movies[0].movieID}/")
    driver.fullscreen_window()
    time.sleep(1)
    try:
        rate = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/div[2]/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[2]/div[2]/div[1]/div[2]/button[1]")))
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[@class='ipc-starbar__rating__button' and @aria-label='Rate {rating}']"))).click()
        rate.click()
        # EC.presence_of_element_located
    except:
        print("ERROR: RATE BUTTON NOT FOUND!")
        unratedList.append((movies[0], rating))
        continue
    time.sleep(2)
    star = driver.find_element(By.XPATH, f".//div[@class='ipc-starbar__rating']/button[@aria-label='Rate {rating}']")
    driver.execute_script("arguments[0].click();", star) 
    rate_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]")
    try:
        rate_button.click()
        time.sleep(2)
    except:
        print("Already Rated!")
        close_prompt = driver.find_element(By.XPATH, "//button[@title='Close Prompt']")
        close_prompt.click()
        time.sleep(1)
    
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Add title to another list']"))).click()
    except:
        print('ERROR: COUD NOT ADD MOVIE TO WATCHED LIST')
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Watched Movies')][@data-titleinlist='false']"))).click()
    except:
        print('Movie is already in the list!')

writefile = open('unratedList', 'w')
print(unratedList, file=writefile)
    
driver.close()
seenList.close()

