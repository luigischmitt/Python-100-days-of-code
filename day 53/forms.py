# CAPSTONE PROJECT - RENTING SF

from selenium import webdriver
from selenium.webdriver.common.by import By
from beautiful_soup import all_addresses, all_links, all_prices
from time import sleep

FORMS = "https://forms.gle/f5FUij62VAky4JHfA"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORMS)

for i in range(0, len(all_addresses)-1):
    sleep(2)
    question1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_but = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    question1.send_keys(all_addresses[i])
    question2.send_keys(all_prices[i])
    question3.send_keys(all_links[i])
    sleep(0.5)
    submit_but.click()
    again = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    again.click()

print("Well done.")
