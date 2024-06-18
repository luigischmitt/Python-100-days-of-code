from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from time import sleep

URL = "https://tinder.com/"

# Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Log-in Process
sleep(2)
login_but = driver.find_element(By.XPATH, '//*[@id="u1584650407"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_but.click()
sleep(1)
facebook_but = driver.find_element(By.XPATH, '//*[@id="u-143730669"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_but.click()
sleep(2)

# Switch to fb window
# It gives us a list of windows = print(driver.window_handles)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
sleep(2)

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
submit_but = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
email_input.send_keys("FB EMAIL")
password_input.send_keys("FB PASSWORD")
sleep(1)
submit_but.click()

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
