class Summa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.sovelluslogiikka.plus(self.io())

class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
    
    def suorita(self):
        self.sovelluslogiikka.miinus(self.io())

class Nollaus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
    
    def suorita(self):
        self.sovelluslogiikka.nollaa()


class Kumoa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.sovelluslogiikka.kumoa()