import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SAVE_DIR = "pages"

# TASK 2: Fetch page
def fetch_page(url):
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# TASK 3: Extract links
def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for tag in soup.find_all("a", href=True):
        absolute_url = urljoin(base_url, tag["href"])
        links.add(absolute_url)

    return links

# TASK 5: Save page
def save_page(html, page_number):
    filename = f"page_{page_number}.html"
    filepath = os.path.join(SAVE_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    return filename

# TASK 4: Crawler loop
def crawl(seed_url, max_pages=5):
    queue = [seed_url]
    visited = set()
    page_count = 0

    while queue and page_count < max_pages:
        current_url = queue.pop(0)

        if current_url in visited:
            continue

        html = fetch_page(current_url)
        if html is None:
            continue

        visited.add(current_url)
        page_count += 1

        filename = save_page(html, page_count)
        print(f"Saved: {filename}")

        links = extract_links(html, current_url)
        print(f"Extracted {len(links)} links")

        for link in links:
            if link not in visited:
                queue.append(link)

    print("Crawling finished!")

# Run crawler
if __name__ == "__main__":
    crawl("https://example.com", max_pages=5)