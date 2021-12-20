from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto


    # def pelaa(self):
    #     tuomari = Tuomari()
    #     tekoaly = TekoalyParannettu(10)

    #     ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
    #     tokan_siirto = tekoaly.anna_siirto()

    #     print(f"Tietokone valitsi: {tokan_siirto}")

    #     while tuomari.onko_ok_siirto(ekan_siirto) and tuomari.onko_ok_siirto(tokan_siirto):
    #         tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    #         print(tuomari)

    #         ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
    #         tokan_siirto = tekoaly.anna_siirto()

    #         print(f"Tietokone valitsi: {tokan_siirto}")
    #         tekoaly.aseta_siirto(ekan_siirto)

    #     print("Kiitos!")
    #     print(tuomari)
