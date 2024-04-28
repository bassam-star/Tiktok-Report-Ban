import requests
from bs4 import BeautifulSoup

def fetch_proxies_from_website(website_url):
    try:
        response = requests.get(website_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        proxies = []
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 2:
                proxy = f"{cols[0].text.strip()}:{cols[1].text.strip()}"
                proxies.append(proxy)
        return proxies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching proxies from website: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    website_url = "https://proxyscrape.com/free-proxy-list"
    proxies = fetch_proxies_from_website(website_url)
    print("Proxies fetched successfully:")
    for proxy in proxies:
        print(proxy)
