import requests
from bs4 import BeautifulSoup

def fetch_cve_data(url):
    """
    Fetches latest CVE data from the provided JSON endpoint.
    Expects each entry to contain 'id' and 'summary'.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        cve_json = response.json()  # Expected to be a list of CVE dicts
        data = []
        for item in cve_json:
            cve_id = item.get('id', 'N/A')
            summary = item.get('summary', '')
            data.append({
                "title": f"CVE: {cve_id}",
                "description": summary
            })
        return data
    except Exception as e:
        print("Error fetching CVE data:", e)
        return []

def fetch_security_reports(url):
    """
    Fetches security alerts from the US-CERT alerts page.
    Parses the HTML content and extracts alert titles and descriptions.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # US-CERT alerts are usually contained in divs with the class 'views-row'
        alerts = soup.find_all('div', class_='views-row')
        data = []
        for alert in alerts:
            title_tag = alert.find(['h2', 'h3'])
            title = title_tag.get_text(strip=True) if title_tag else "US-CERT Alert"
            description = alert.get_text(" ", strip=True)
            data.append({
                "title": title,
                "description": description
            })
        return data
    except Exception as e:
        print("Error fetching security reports:", e)
        return []

def fetch_forum_posts(url):
    """
    Fetches forum posts from Reddit's NetSec subreddit.
    Uses a proper user agent to avoid being blocked by Reddit.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; CyberSecBot/1.0; +http://yourdomain.com/bot)"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Attempt to extract posts by searching for div elements with class 'thing'
        posts = soup.find_all('div', class_='thing')
        data = []
        for post in posts:
            title_tag = post.find('a', class_='title')
            if title_tag:
                title = title_tag.get_text(strip=True)
                description = post.get_text(" ", strip=True)
                data.append({
                    "title": f"Reddit Post: {title}",
                    "description": description
                })
        return data
    except Exception as e:
        print("Error fetching forum posts:", e)
        return []

def fetch_all_data(urls):
    """
    Fetches data from all sources defined in the urls dictionary.
    """
    cve_data = fetch_cve_data(urls.get("cve"))
    reports = fetch_security_reports(urls.get("reports"))
    forums = fetch_forum_posts(urls.get("forums"))
    return cve_data + reports + forums

if __name__ == "__main__":
    from config import SCRAPE_URLS
    all_data = fetch_all_data(SCRAPE_URLS)
    print("Fetched data:")
    for item in all_data:
        print(item)
