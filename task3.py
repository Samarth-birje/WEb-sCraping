import requests
from bs4 import BeautifulSoup
import sys

URL = "https://www.bbc.com/"
OUTPUT_FILE = "headline.txt"

def fetch_headlines():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,'html.parser')

    headline_tags = soup.select("h1, h2")

    headlines = []

    for tag in headline_tags:
        text = tag.get_text(strip=True)
        if text and len(text) > 5:        
            headlines.append(text)

    return headlines

def save_headlines(headlines):
    if not headlines:
        print("no headlines to save")
        return
    
    try:
        with open(OUTPUT_FILE, 'w' , encoding='utf-8') as f:
            for line in headlines:
                f.write(f"{line}\n")
        print(f"Successfully saved {len(headlines)} headlines to {OUTPUT_FILE}")
    except IOError as e:
        print(f"Error writing to file {OUTPUT_FILE}: {e}")
        sys.exit(1)

scraped_headlines = fetch_headlines()
save_headlines(scraped_headlines)
