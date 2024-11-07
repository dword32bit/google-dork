import argparse
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

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            if "Our systems have detected unusual traffic" in response.text:
                print("Blocked by Google. Try again later or adjust your query.")
                return []
            return self.parse_results(response.text)
        else:
            print(f"Failed to fetch results, status code: {response.status_code}")
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

def main():
    parser = argparse.ArgumentParser(description="Google Dorking CLI Tool without API")
    parser.add_argument("-d", "--domain", type=str, help="Domain to target, e.g., example.com")
    parser.add_argument("-f", "--filetype", type=str, help="Filetype to search, e.g., pdf, xlsx")
    parser.add_argument("-t", "--intext", type=str, help="Text to search within files, e.g., sensitive data")
    parser.add_argument("-i", "--intitle", type=str, help="Title text to search, e.g., login page")
    parser.add_argument("-u", "--inurl", type=str, help="URL text to search, e.g., admin")

    args = parser.parse_args()

    dork = GoogleDork(
        domain=args.domain,
        filetype=args.filetype,
        intext=args.intext,
        intitle=args.intitle,
        inurl=args.inurl
    )

    results = dork.search()
    dork.display_results(results)

if __name__ == "__main__":
    main()
