# INSTAGRAM REJECT FOLLOWER'S INVITE

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = "https://www.instagram.com/"
USERNAME = ""
PASSWORD = ""

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Login Process
sleep(3)
username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
sleep(0.5)
login_button.click()

# Bot Process
sleep(6)
heart_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[6]/div/span')
heart_button.click()
sleep(2)
followers_invite = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/span')
followers_invite.click()

delete_invite = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div[3]/div[2]')
delete_invite.click() # You can put a for range to delete all invitations
