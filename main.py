from Models import Internet_shop
from Models.Citilink import Citilink


class JobWithShop:
    def __init__(self):
        self._shop: Internet_shop = Citilink(0)

    def parse_shop(self):
        self._shop.selenium_start()
        self._shop.parse_notebook_list(self._shop.find_last_page())
        self._shop.selenium_quit()
        return self._shop.notebooks


proverka1 = JobWithShop()
list1 = proverka1.parse_shop()[0:10]
for element in list1:
    print(str(element))

