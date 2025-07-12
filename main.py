from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import requests
import os
import time
from googletrans import Translator
from collections import Counter
import re

# Setup Chrome WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Save image locally
def save_image(img_url, title):
    if img_url.startswith("http"):
        filename = f"screenshots/{title[:20].replace(' ', '_')}.jpg"
        response = requests.get(img_url)
        with open(filename, "wb") as f:
            f.write(response.content)

# Scrape El País Opinion Articles
def scrape_articles():
    driver = setup_driver()
    driver.get("https://elpais.com/opinion/")
    time.sleep(3)

    # Step 1: Grab first 5 article links
    links = []
    all_links = driver.find_elements(By.CSS_SELECTOR, 'article a')
    for link in all_links:
        href = link.get_attribute('href')
        if href and href.startswith("https://elpais.com/opinion") and href not in links:
            links.append(href)
        if len(links) == 5:
            break

    scraped_data = []

    # Step 2: Visit each article
    for url in links:
        try:
            driver.get(url)
            time.sleep(4)

            title = driver.find_element(By.TAG_NAME, "h1").text

            try:
                content = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-dtm-region="articulo-cuerpo"]'))
                ).text
            except:
                content = "Content not found"

            try:
                img = driver.find_element(By.CSS_SELECTOR, "figure img").get_attribute("src")
                save_image(img, title)
            except:
                img = "No image found"

            scraped_data.append({
                "title": title,
                "content": content,
                "image": img
            })

            print("\n✅ Article scraped:")
            print("Title:", title)
            print("Image:", img)

        except Exception as e:
            print("❌ Error scraping article:", e)
            continue

    driver.quit()
    return scraped_data

# Translate Titles to English
def translate_titles(articles):
    translator = Translator()
    translated = []
    print("\n🔄 Translating titles:")
    for art in articles:
        orig = art["title"]
        try:
            eng = translator.translate(orig, src="es", dest="en").text
        except:
            eng = "Translation failed"
        translated.append(eng)
        print(f'  • "{orig}" → "{eng}"')
    return translated

# Analyze Word Frequency
def analyze_translated(translated_titles):
    print("\n📊 Word Frequency (count > 2):")
    words = []
    for t in translated_titles:
        words += re.findall(r"\w+", t.lower())
    freq = Counter(words)
    found = False
    for w, c in freq.items():
        if c > 2:
            found = True
            print(f"  • {w} — {c} times")
    if not found:
        print("  • No repeated words more than twice.")

# Main Flow
if __name__ == "__main__":
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    articles = scrape_articles()
    translated_titles = translate_titles(articles)
    analyze_translated(translated_titles)
