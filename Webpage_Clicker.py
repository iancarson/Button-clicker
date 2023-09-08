from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

# Set the URL of the webpage you want to interact with
url = "https://combustibleapp.com/#/pages/index/index"  # Replace with your target URL
//Define the login credentials
username = "username"
password = "password"


# Create a function to automate the interaction
def automate_interaction():
    # Initialize a Selenium WebDriver
    driver = webdriver.Chrome()  # You need to have ChromeDriver installed

    try:
        # Open the webpage
        driver.get(url)

        # Find and click the button on the webpage
        button = driver.find_element(By.XPATH,"//button[contains(text(), 'Button Text')]")  # Replace with the actual button locator
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
