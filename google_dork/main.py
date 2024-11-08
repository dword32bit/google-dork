import requests
from bs4 import BeautifulSoup
import urllib.parse
import random
import time

class GoogleDork:
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    ]

    def __init__(self, domain=None, filetype=None, intext=None, intitle=None, inurl=None):
        self.domain = domain
        self.filetype = filetype
        self.intext = intext
        self.intitle = intitle
        self.inurl = inurl

    def build_query(self):
        query = ""
        if self.domain:
            query += f"site:{self.domain} "
        if self.filetype:
            query += f"filetype:{self.filetype} "
        if self.intext:
            query += f'intext:"{self.intext}" '
        if self.intitle:
            query += f'intitle:"{self.intitle}" '
        if self.inurl:
            query += f'inurl:"{self.inurl}" '
        return urllib.parse.quote(query.strip())

    def search(self):
        query = self.build_query()
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": random.choice(self.USER_AGENTS)
        }

        print(f"Executing Google Dorking with query: {urllib.parse.unquote(query)}")

        time.sleep(random.uniform(1, 3))

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            if "Our systems have detected unusual traffic" in response.text:
                print("Blocked by Google. Try again later or adjust your query.")
                return []
            return self.parse_results(response.text)
        except requests.RequestException as e:
            print(f"Error during request: {str(e)}")
            return []

    def parse_results(self, html):
        soup = BeautifulSoup(html, "html.parser")
        results = []

        for g in soup.find_all('div', class_='tF2Cxc'):
            title = g.find('h3').text if g.find('h3') else "No title"
            link_tag = g.find('a', href=True)
            if link_tag:
                link = link_tag['href']
                results.append({"title": title, "link": link})

        return results

    def display_results(self, results):
        if results:
            print("\nGoogle Dorking Results:")
            for result in results:
                print(f"Title: {result['title']}")
                print(f"Link: {result['link']}")
                print("-" * 80)
        else:
            print("No results found.")
