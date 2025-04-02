"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case demonstrates how to automate filling out and submitting a web form using Selenium.
The script inputs text into various fields, selects options from dropdown menus, checks and unchecks checkboxes and radio buttons, picks a color and date, adjusts a range slider using JavaScript, and uploads a local PDF file.
It captures screenshots both before and after form submission for verification.
This example highlights Selenium’s ability to handle different types of form elements and introduces basic DOM interaction, condition checking, and JavaScript execution for complex controls.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# Launch browser (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the form page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Wait for the form to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

# Fill out text fields
driver.find_element(By.NAME, "my-text").send_keys("Luke Tam")
driver.find_element(By.NAME, "my-password").send_keys("TestPassword123!")
driver.find_element(By.NAME, "my-textarea").send_keys("This is a test message.")
driver.find_element(By.NAME, "my-datalist").send_keys("Boston")

# Select from dropdown
select = Select(driver.find_element(By.NAME, "my-select"))
select.select_by_visible_text("Two")

# Select a file
file_path = os.path.abspath("../Data/3 - Mid-Term Instructions.pdf")
driver.find_element(By.NAME, "my-file").send_keys(file_path)

# Unselect a checkbox
checked_checkbox = driver.find_element(By.ID, "my-check-1")
if checked_checkbox.is_selected():
    checked_checkbox.click()

# Select a checkbox
default_checkbox = driver.find_element(By.ID, "my-check-2")
if not default_checkbox.is_selected():
    default_checkbox.click()

# Select a radio button
default_radio = driver.find_element(By.ID, "my-radio-2")
if not default_radio.is_selected():
    default_radio.click()

# Select a color
driver.find_element(By.NAME, "my-colors").send_keys("#008000")

# Select a date
driver.find_element(By.NAME, "my-date").send_keys("04/01/2025")
driver.find_element(By.NAME, "my-date").send_keys(Keys.TAB)  # hide the calendar popup

# Set slider value using JavaScript
slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value = arguments[1];", slider, "8")

# Take a screenshot of the filled form
driver.save_screenshot("../Screenshots/3 - Web Form Completed.png")

# Submit the form
driver.find_element(By.TAG_NAME, "button").click()

# Take a screenshot of the confirmation page
time.sleep(2)
driver.save_screenshot("../Screenshots/3 - Web Form Confirmation.png")

# Display success message
print('✅ Success! Screenshots of the completed web form and the confirmation page have been saved in the "Screenshots" folder.')

# Close the browser
driver.quit()