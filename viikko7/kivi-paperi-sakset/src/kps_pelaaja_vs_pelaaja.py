from tuomari import Tuomari
from kps import KPS

# selvitä miten pelin aikana syntyvät tulosteet toimii eri luokissa
class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto
