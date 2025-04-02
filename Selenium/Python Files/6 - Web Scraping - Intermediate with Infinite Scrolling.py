"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case demonstrates how to use Selenium to scrape dynamically loaded content from a webpage with infinite scrolling.
The script navigates to the Quotes to Scrape site, scrolls to the bottom repeatedly until all content is loaded, and then extracts the text, author, and tags of each quote.
This example introduces a common scrolling automation pattern using JavaScript and shows how to detect when no new content is being added.
It's a practical example for handling social feeds, product catalogs, or any website that loads additional items as the user scrolls.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# Launch browser (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the quotes page
driver.get("https://quotes.toscrape.com/scroll")

# Wait for initial content
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

# Scroll loop
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to bottom of page and wait briefly for new content to load
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # No more new content loaded
    last_height = new_height

# Get all quotes
quotes = driver.find_elements(By.CLASS_NAME, "quote")

print(f"Total quotes loaded: {len(quotes)}\n")

# Display first 10 quotes
for i, quote in enumerate(quotes[:10], start=1):
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
    print(f"{i}. {text}")
    print(f"   — {author}")
    print(f"   Tags: {', '.join(tags)}\n")

# Close the browser
driver.quit()