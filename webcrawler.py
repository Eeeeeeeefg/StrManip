import requests
import bs4


class Crawler:
    """This will search for a document and parse it into a plain text file"""
    def __init__(self):
        self.encoding = 'utf-8'
        self.links = {}
        self.scrape_results = {}

    def link_add(self, link_name: str, link: str):
        self.links.update({link_name: link})

    def scrape(self):
        for i in self.links.items():
            r = requests.get(i[1])
            self.scrape_results.update({i[0]: r.text})

    def soupify(self):
        soup = {}
        for i in self.scrape_results.items():
            soup.update({i[0]: bs4.BeautifulSoup(i[1], features='html.parser')})
        return soup
