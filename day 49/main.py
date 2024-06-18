from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# Cancel the apply
def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sign_in_but = driver.find_element(By.XPATH, "/html/body/div[2]/a[1]")
sleep(3) # Pause to load
sign_in_but.click()

email_input = driver.find_element(By.XPATH, '//*[@id="username"]')
password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
submit_but = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

email_input.send_keys("EMAIL")
password_input.send_keys("PASSWORD")
sleep(1)
submit_but.click()

sleep(3)
first_job = driver.find_element(By.XPATH, '//*[@id="ember220"]')
first_job.click()

# Get Listings
sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("PHONE")

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()
