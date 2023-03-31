from LaptopUtilities.Internet_shop import InternetShop
from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from LaptopUtilities.NotebookSpecs import NotebookSpecs


class Citilink(InternetShop):
    def __init__(self, i):
        self.host = 'https://www.citilink.ru'
        self.url = 'https://www.citilink.ru/catalog/noutbuki/?view_type=grid&f=discount.any%2Crating.any'
        self.prices: List[int] = super().prices_list[i-1]
        self.price_segment = i
        self.driver = webdriver.Chrome()
        self.notebooks: List[NotebookSpecs] = []

    def find_last_page(self):
        last_page = self.driver.find_element(By.XPATH,
                                             "//div[@class='PaginationWidget__wrapper-pagination']/a[last()-1]")
        return int(last_page.text)

    def parse_notebook_list(self, max_pages):
        i = 0
        while i < max_pages:
            try:
                content = BeautifulSoup(self.driver.page_source, 'html.parser')
                items = content.find_all('div',
                                         class_="ProductCardVerticalLayout__wrapper-description ProductCardVertical__layout-description")
                for item in items:
                    data = item.find('a', class_="ProductCardVertical__name Link js--Link Link_type_default")
                    self.notebooks.append(NotebookSpecs(data_string=data.get('title').replace("\'", ""),
                                                        shop='Citilink',
                                                        link=self.host + data.get('href')))
                    i += 1
                self.driver.get(self.url + "&p=" + str(i))
                if self.driver.current_url == "https://www.citilink.ru/catalog/":
                    raise Exception
            except Exception:
                print("exception Citilink")
                break

    def make_url_with_prices(self):
        self.url = self.url + "&price_max=" + self.prices[1] + \
                   "&pprice_max=" + self.prices[1] + "&price_min=" + self.prices[0]




