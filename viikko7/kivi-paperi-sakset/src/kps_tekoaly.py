from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
        
    # def pelaa(self):
    #     tuomari = Tuomari()
    #     tekoaly = Tekoaly()

    #     ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
    #     tokan_siirto = tekoaly.anna_siirto()

    #     print(f"Tietokone valitsi: {tokan_siirto}")

    #     while tuomari.onko_ok_siirto(ekan_siirto) and tuomari.onko_ok_siirto(tokan_siirto):
    #         tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    #         print(tuomari)

    #         ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
    #         tokan_siirto = tekoaly.anna_siirto()

    #         print(f"Tietokone valitsi: {tokan_siirto}")

    #     print("Kiitos!")
    #     print(tuomari)
