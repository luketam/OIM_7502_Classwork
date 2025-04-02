"""
Name: Luke Tam
Library: Selenium
Documentation URL: https://www.selenium.dev/documentation/
Use Case Description:
This use case presents a complete end-to-end automation pipeline using Selenium, pandas, matplotlib, and wordcloud.
The script scrapes the first three news articles from NPR, extracts and cleans the full article text, identifies the top 10 most frequent non-stopwords for each article, and saves the results to a single Excel file.
It also generates a bar chart and word cloud for each article, visualizing the most common words based on the full article content.
This use case showcases the integration of web scraping, text processing, data visualization, and file output into a cohesive and reproducible automation workflow.
"""

from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import nltk
from nltk.corpus import stopwords
import os
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from wordcloud import WordCloud

# one-time download of NLTK stopwords
# nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Create output folders if they do not already exist
os.makedirs("Data", exist_ok=True)
os.makedirs("Charts", exist_ok=True)

# ---------------------------
# Step 1: Open NPR News and get first 3 article links
# ---------------------------
# Launch browser (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open NPR News and wait for headlines to load
driver.get("https://www.npr.org/sections/news/")
time.sleep(3)

# Get the first 3 article links
headline_elements = driver.find_elements(By.CSS_SELECTOR, 'h2.title a')
articles = []
seen = set()
all_data = []

for elem in headline_elements:
    title = elem.text.strip()
    url = elem.get_attribute("href")

    if title and url and url not in seen:
        articles.append((title, url))
        seen.add(url)

    if len(articles) == 3:
        break

# ---------------------------
# Step 2: Process each article
# ---------------------------
for i, (title, url) in enumerate(articles, start=1):
    print(f"🔍 Processing article {i}: {title}")
    driver.get(url)
    time.sleep(3)

    # Try to extract article paragraphs
    try:
        paragraphs = driver.find_elements(By.CSS_SELECTOR, 'div.storytext p')
        article_text = " ".join([p.text.strip() for p in paragraphs])
    except:
        print("❌ Failed to extract article body.")
        continue

    # Clean and tokenize article text
    text = article_text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    filtered_words = [w for w in words if w not in stop_words and len(w) > 2]

    # Count top 10 words
    word_freq = Counter(filtered_words)
    top_words = word_freq.most_common(10)

    # Store article details and word frequencies
    for word, count in top_words:
        all_data.append({
            "Article #": i,
            "Headline": title,
            "URL": url,
            "Word": word,
            "Frequency": count
        })

    # ---------------------------
    # Step 3: Create bar chart
    # ---------------------------
    words, counts = zip(*top_words)
    plt.figure(figsize=(8, 5))
    plt.bar(words, counts, color="green")
    plt.title(f"Top Words in Article {i}")
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.tight_layout()
    bar_filename = f"../Charts/8 - Article {i} Top 10 Words.png"
    plt.savefig(bar_filename)
    plt.close()

    # ---------------------------
    # Step 4: Create word cloud
    # ---------------------------
    wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(filtered_words))
    wc_filename = f"../Charts/8 - Article {i} Word Cloud.png"
    wc.to_file(wc_filename)

# ---------------------------
# Step 5: Save all collected data to one Excel file
# ---------------------------
df_all = pd.DataFrame(all_data)
excel_filename = "../Data/8 - NPR News Top 10 Words.xlsx"
df_all.to_excel(excel_filename, index=False)

# Display success message
print("✅ Success! Headlines scraped. Excel saved. Bar charts and word clouds generated!")

# Close the browser
driver.quit()