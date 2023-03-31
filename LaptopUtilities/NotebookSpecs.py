

class NotebookSpecs:
    def __init__(self, data_string: str, shop: str, link: str):
        self.link = link
        self.shop = shop
        self.cpu_score: int = None
        self.gpu_score: int = None
        self.ram_score: int = None
        self.rom_score: int = None
        self.score: int = None
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
            if data_strings[2] not in ['  AMOLED', '  IPS', '  LTPS', '  OLED', '  TN']:
                number = 2
            else:
                number = 3
            self.cpu = data_strings[number][1:].lower()
            self.ram = data_strings[number+1][1:].lower()
            self.rom = data_strings[number+2][1:].lower()
            self.gpu = data_strings[number+3][1:-1].lower()

    def __str__(self):
        return f'Notebook with cpu {self.cpu}, gpu {self.gpu} and link is {self.link}'



