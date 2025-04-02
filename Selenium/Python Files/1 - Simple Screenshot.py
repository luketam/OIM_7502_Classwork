"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case demonstrates how to automate the process of capturing a webpage screenshot using Selenium.
The script launches a Chrome browser, navigates to the official Selenium website, waits briefly for the page to load, and saves a full-page screenshot to a designated folder.
This introduces basic Selenium commands such as launching the browser, navigating to a URL, and using save_screenshot() for visual documentation or testing purposes.
While it uses a simple time.sleep() for page loading, future use cases will incorporate more robust waiting strategies.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager

# Launch browser (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://www.selenium.dev/")

# Wait for page to load (better to use WebDriverWait in later use cases)
time.sleep(2)

# Take a screenshot
driver.save_screenshot("../Screenshots/1 - Webpage Screenshot.png")

# Display success message
print('✅ Success! A screenshot of the webpage has been saved in the "Screenshots" folder.')

# Close browser
driver.quit()