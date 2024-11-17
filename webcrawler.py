import requests
import bs4


class Crawler:
    """This will search for a document and parse it into a plain text file"""
    def __init__(self):
        self.encoding = 'utf-8'
        self.links = {}
        self.scrape_results = []

    def link_add(self, link_name: str, link: str):
        self.links.update({link_name: link})

    def scrape(self):
        for i in self.links.values():
            r = requests.get(i)
            self.scrape_results.append(r.text)

    def soupify(self):
        soup = []
        for i in self.scrape_results:
            soup.append(bs4.BeautifulSoup.get_text(i))
        return soup
