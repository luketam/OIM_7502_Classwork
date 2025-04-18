# Python Library Showcase: Selenium

This project showcases a series of progressively more complex use cases using **Selenium** in Python to automate browser tasks and extract data from websites. The goal is to demonstrate how Selenium can be applied to real-world business and data analytics scenarios, ranging from simple automation to full end-to-end data pipelines.

Developed as part of a graduate course in **Advanced Programming for Business Analytics** at Babson College, this project highlights practical techniques for web interaction, data scraping, and content analysis.

---

## What Is Selenium?

Selenium is a powerful Python library for automating web browsers. It simulates real user behavior—clicking, typing, scrolling, and navigating—to interact with dynamic websites and extract data that may not be accessible through static HTML alone.

---

## Tools and Libraries Used

- `selenium` – browser automation  
- `pandas` – data storage and export (Excel/CSV)  
- `matplotlib` – data visualization (bar charts)  
- `wordcloud` – natural language visualization  
- `nltk` – stopword removal for text cleaning  
- `os`, `time`, `re` – support for file handling, delays, and regex  
- `webdriver_manager` – automatic ChromeDriver setup  

---

## Use Case Overview

This project includes **8 structured use cases**, progressing from simple browser actions to complex scraping and analysis workflows:

| Use Case | Title                                               | Description |
|----------|-----------------------------------------------------|-------------|
| 1        | Simple Screenshot                                   | Capture a full-page screenshot of a website |
| 2        | Account Login                                       | Automate logging into a website using a sample username and password |
| 3        | Web Form                                            | Fill out and submit a form with various input types |
| 4        | Web Scraping - Basic                                | Extract headlines from NPR News |
| 5        | Web Scraping - Intermediate                         | Scrape product data from OpenFoodFacts.org |
| 6        | Web Scraping - Intermediate with Infinite Scrolling | Load and scrape all quotes from a scrollable page |
| 7        | Web Scraping - Advanced                             | Scrape jobs and descriptions from Indeed using multi-tab logic |
| 8        | End-to-End Automation                               | Scrape and analyze news content with charts and word clouds |

---

## How to Run the Code

1. **Install the required Python libraries**  
   Use pip to install the following packages:  
   selenium, pandas, matplotlib, wordcloud, nltk, and webdriver-manager

2. **Download the Chrome browser** (if not already installed)  
   Selenium uses ChromeDriver to control Chrome, so having Chrome installed is required.

3. **Open the Jupyter Notebook**  
   Launch Jupyter Notebook from your terminal or Anaconda Navigator, then open `Selenium Tutorial.ipynb`.  
   From there, you can run each use case interactively in order.