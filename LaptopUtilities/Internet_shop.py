from typing import List
from selenium import webdriver
from LaptopUtilities.NotebookSpecs import NotebookSpecs


class InternetShop:
    driver: webdriver
    prices_list: List[List[int]] = [[0, 30000], [30000, 50000], [50000, 70000], [70000, 100000]]

    def __init__(self):
        host: str
        url: str
        notebooks: List[NotebookSpecs]

    def selenium_start(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def parse_notebook_list(self, max_pages):
        pass

    def find_specs(self):
        pass

    def find_last_page(self):
        pass

    def __init__(self):
        pass

    def selenium_quit(self):
        self.driver.quit()
