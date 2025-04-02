"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case demonstrates advanced web scraping techniques by collecting job postings from Indeed using a live Chrome session with remote debugging.
The script navigates through the first three pages of job search results for Business Analyst positions in Boston and extracts detailed information for the first two jobs on each page.
For each job, it captures the job title, company, location, URL, and full job description, then saves the structured data to an Excel file.
This example highlights multi-page scraping, browser tab management, dynamic content handling with explicit waits, and the use of remote browser control to bypass bot detection and CAPTCHA restrictions.
"""

# ============================== #
# INSTRUCTIONS BEFORE RUNNING THIS SCRIPT
# ============================== #
#
# STEP 1: Manually start Google Chrome with remote debugging enabled.
#         This allows Selenium to attach to your existing browser session.
#
# WINDOWS:
# Open Command Prompt and run (include all quotes):
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome_temp"
#
# macOS:
# Open Terminal and run (include all quotes):
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_temp"
#
# STEP 2: Run the following Python script.

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome to attach to the existing session
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Connect to the existing Chrome session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the Indeed job search page (adjust filters in URL as needed)
# Job title: Business Analyst
# Location: Boston, MA
# Date posted: Last 7 days
base_url = "https://www.indeed.com/jobs?q=business+analyst&l=Boston%2C+MA&fromage=7&start={}"
results = []

# Loop through first 3 pages (0, 10, 20)
for page in range(0, 30, 10):
    driver.get(base_url.format(page))
    driver.refresh()
    time.sleep(3)

    # Wait for all job cards on the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job_seen_beacon")))

    # Get all job cards on the page
    job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

    # Loop through first 2 jobs on the page
    for card in job_cards[:2]:
        try:
            # Extract job title, company, and location
            title = card.find_element(By.TAG_NAME, "h2").text.strip()
            company = card.find_element(By.CSS_SELECTOR, 'span[data-testid="company-name"]').text.strip()
            location = card.find_element(By.CSS_SELECTOR, 'div[data-testid="text-location"]').text.strip()

            # Build full job URL to get job description
            link = card.find_element(By.TAG_NAME, "a")
            href = link.get_attribute("href")
            job_url = href if href.startswith("http") else "https://www.indeed.com" + href

            # Open job details page in new tab and wait for page to laod
            driver.execute_script("window.open(arguments[0]);", job_url)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)

            # Extract job description
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jobDescriptionText")))
            description = driver.find_element(By.ID, "jobDescriptionText").text.strip()

            # Save results as list of dictionraries
            results.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "URL": job_url,
                "Description": description
            })

            # Close job details tab and switch back to search window
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except:
            continue

# Make sure the destination folder exists
os.makedirs("Data", exist_ok=True)

# Convert list of job dictionaries to DataFrame
df = pd.DataFrame(results)

# Save to Excel
excel_filename = "../Data/7 - Indeed Job Postings.xlsx"
df.to_excel(excel_filename, index=False)

# Display success message
print('✅ Success! The job details have been saved in the "Data" folder.')

# Manually close the Chrome window