"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case demonstrates intermediate-level web scraping using Selenium by extracting structured product data from OpenFoodFacts.org.
The script loads the main product listing page, waits for the content to finish loading, and collects the name, URL, and nutritional labels (Nutri-Score, NOVA group, and Green-Score) for the first 10 food products.
It showcases how to work with nested HTML elements, extract image metadata for additional context, and apply conditional logic to parse available product information.
This example strengthens your understanding of navigating real-world HTML structures and processing mixed content types.
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

# Open OpenFoodFacts.org
driver.get("https://world.openfoodfacts.org/")

# Wait until products finish loading
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#products_match_all li")))

# Get list of products
products = driver.find_elements(By.CSS_SELECTOR, "#products_match_all li")

# Scrape first 10 items
print("First 10 Products on OpenFoodFacts.org:\n")
for i, item in enumerate(products[:10], start=1):

    # Get name and link
    link_tag = item.find_element(By.TAG_NAME, "a")
    name = link_tag.text.strip()
    link = link_tag.get_attribute("href")

    # Get all images and parse score info
    images = item.find_elements(By.TAG_NAME, "img")
    nutri_score = nova = green_score = "N/A"
    for img in images:
        src = img.get_attribute("src")
        title = img.get_attribute("title")
        if src:
            if "nutriscore" in src:
                nutri_score = (title.replace("Nutri-Score ", "")
                               .replace("unknown", "Unknown"))
            elif "nova-group" in src:
                nova = (title.replace("NOVA ", "")
                        .replace("not computed", "Not computed"))
            elif "green-score" in src:
                green_score = (title.replace("Green-Score ", "")
                               .replace("not applicable", "Not applicable")
                               .replace("not computed", "Not computed"))

    # Display product info
    print(f"{i}. {name}")
    print(f"   Link: {link}")
    print(f"   Nutri-Score: {nutri_score}")
    print(f"   NOVA Group: {nova}")
    print(f"   Green-Score: {green_score}")
    print()

# Close the browser
driver.quit()