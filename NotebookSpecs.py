

class NotebookSpecs:
    cpu: str
    gpu: str
    ram: str
    rom: str
    link: str
    shop: str
    cpu_score: int = None
    gpu_score: int = None
    score: int = None

    def __init__(self, data_string: str, shop: str, link: str):
        self.link = link
        self.shop = shop
        if shop == 'DNS':
            data_string = data_string.replace("/", "")
            data_string = data_string.replace("<span>", "")
            data_strings = data_string.split(',')
            data_strings[2] = data_strings[2].replace(" ", "-")
            self.cpu = data_strings[2][1:].lower()
            self.ram = data_strings[4][1:].lower()
            if len(data_strings) == 8:
                self.gpu = data_strings[6][1:-1].lower()
                self.rom = data_strings[5][1:].lower()
            if len(data_strings) == 9:
                self.gpu = data_strings[7][1:-1].lower()
                self.rom = data_strings[5][1:].lower() + ' ' + data_strings[6][1:].lower()
        if shop == 'Citilink':
            data_strings = data_string.split(',')
            data_strings[2] = data_strings[2].replace(" ", "-")
            self.cpu = data_strings[3][1:].lower()
            self.ram = data_strings[4][1:].lower()
            self.rom = data_strings[5][1:].lower()
            self.gpu = data_strings[6][1:-1].lower()



