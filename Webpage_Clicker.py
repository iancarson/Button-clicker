from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

url = "https://combustibleapp.com/#/pages/index/index" 
username = "username"
password = "password"

def automate_interaction():
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        login_prompt = driver.find_elements(By.XPATH, "//input[@type='text' and @name='username']")
        if login_prompt:
            #If a login prompt is found, enter the credentials.
            username_input = driver.find_elements(By.XPATH, "//input[@type='text' and @name='username']")
            password_input = driver.find_elements(By.XPATH, "//input[@type='password' and @name='password']")
            login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
            username_input.send_keys(username)
            password_input.send_keys(password)
            login_button.click()
        else:
            button = driver.find_element(By.XPATH,"//button[contains(text(), 'Button Text')]")
            button.click()
        # Wait for a few seconds (adjust the time as needed)
        time.sleep(2)

        # Handle the popup
        alert = Alert(driver)
        alert.accept()  # Click the OK button on the popup

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the browser window
        driver.quit()


# Repeat the interaction 40 times a day
for _ in range(40):
    automate_interaction()
    time.sleep(86400)  # Wait for 24 hours (60 seconds * 60 minutes * 24 hours)
