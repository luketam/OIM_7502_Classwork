"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case demonstrates how to automate the process of logging into a website using Selenium.
The script navigates to a sample login page, waits for the login form to load, enters a predefined username and password, submits the form, and waits for confirmation of a successful login.
It concludes by capturing a screenshot of the post-login page.
This example introduces form interaction, button clicks, and the use of explicit waits to ensure that elements are fully loaded before interacting with them.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# Launch browser (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the login page
driver.get("https://the-internet.herokuapp.com/login")

# Wait for the login form to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

# Fill in username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click the login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for the login to complete and dashboard to appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flash.success")))

# Save screenshot
driver.save_screenshot("../Screenshots/2 - Account Login.png")

# Display success message
print('✅ Success! A screenshot of the webpage after logging in has been saved in the "Screenshots" folder.')

# Close the browser
driver.quit()