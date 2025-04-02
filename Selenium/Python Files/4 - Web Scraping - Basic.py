"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case introduces basic web scraping with Selenium by extracting news headlines from the NPR News website.
The script launches a browser, navigates to the NPR News section, waits for the page content to load, and collects the text of the first 10 headline links using CSS selectors.
It demonstrates fundamental scraping techniques such as locating elements by tag and class, handling dynamic page loading with explicit waits, and iterating over results to extract and display clean text output.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Launch browser (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the NPR News section
driver.get("https://www.npr.org/sections/news/")
driver.maximize_window()

# Wait until headline links are loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.title a")))

# Grab all headline elements
headline_elements = driver.find_elements(By.CSS_SELECTOR, "h2.title a")

# Extract and print their text content
print("Top 10 Headlines on NPR News:\n")
for i, element in enumerate(headline_elements[:10], start=1):
    print(f"{i}. {element.text}")

# Close the browser
driver.quit()