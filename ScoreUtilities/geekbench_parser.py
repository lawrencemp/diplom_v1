import requests
from bs4 import BeautifulSoup


class CpuScoreParser():
    HOST = 'https://browser.geekbench.com'
    URL = 'https://browser.geekbench.com/processors/'

    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'

    }

    @classmethod
    def get_html(cls, params=''):
        r = requests.get(cls.URL, headers=cls.HEADERS, params=params)
        return r

    @staticmethod
    def get_cpu_score(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find('div', class_="score-container desktop")
        item = items.find('div', class_="score")
        return item.text


