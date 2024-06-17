from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

menu = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')

lista = menu.find_elements(By.TAG_NAME, "li")

time = []
name = []

for item in lista:
    time.append(item.find_element(By.TAG_NAME, "time").text)

for item in lista:
    name.append(item.find_element(By.TAG_NAME, "a").text)

my_dict = {}

for n in range(len(lista)):
    my_dict[n] = {
        "time": time[n],
        "name": name[n]
    }

print(my_dict)
 
driver.quit()
