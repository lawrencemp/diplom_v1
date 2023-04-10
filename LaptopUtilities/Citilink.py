from selenium.common import NoSuchElementException
from LaptopUtilities.Internet_shop import InternetShop
from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from LaptopUtilities.NotebookSpecs import NotebookSpecs


class Citilink(InternetShop):
    def __init__(self, i):
        self.host = 'https://www.citilink.ru'
        self.url = 'https://www.citilink.ru/catalog/noutbuki/?view_type=list&f=discount.any%2Crating.any'
        self.prices: List[int] = super().prices_list[i - 1]
        self.price_segment = i
        self.driver = webdriver.Chrome()
        self.notebooks: List[NotebookSpecs] = []

    def find_last_page(self):
        try:
            last_page = self.driver.find_element(By.XPATH,
                                                 '//div[@data-meta-name="Pagination"]/div[last()]/a[last()-1]')
        except NoSuchElementException:
            return 1
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", last_page)
        return int(last_page.text)

    def parse_notebook_list(self, max_pages):
        i = 0
        while i < max_pages:
            try:
                laptop_cards = self.driver.find_elements(By.XPATH,
                                                         '//div[@data-meta-name="SnippetProductHorizontalLayout"]//a['
                                                         'contains(@title,"бук")]')
                for laptop_card in laptop_cards:
                    data = laptop_card.text
                    self.notebooks.append(
                        NotebookSpecs(data_string=data.replace("\'", ""), shop='Citilink',
                                      link=laptop_card.get_attribute('href')))
                i += 1
                self.driver.get(self.url + "&p=" + str(i))
                if self.driver.current_url == "https://www.citilink.ru/catalog/":
                    raise Exception
            except Exception:
                print("exception Citilink")
                break

    def make_url_with_prices(self):
        self.url = self.url + "&price_max=" + str(self.prices[1]) + \
                   "&pprice_max=" + str(self.prices[1]) + "&price_min=" + str(self.prices[0])
