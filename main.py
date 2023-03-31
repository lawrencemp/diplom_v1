from LaptopUtilities.Internet_shop import InternetShop
from LaptopUtilities.Citilink import Citilink


class JobWithShop:
    def __init__(self):
        self._shop: InternetShop = Citilink(1)

    def parse_shop(self):
        self._shop.selenium_start()
        self._shop.parse_notebook_list(self._shop.find_last_page())
        self._shop.selenium_quit()
        return self._shop.notebooks


proverka1 = JobWithShop()
list1 = proverka1.parse_shop()[0:10]
for element in list1:
    print(str(element))

