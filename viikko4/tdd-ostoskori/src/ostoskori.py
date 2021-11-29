from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maarat = map(lambda o: o.lukumaara(), self._ostokset)
        return sum(maarat)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinnat = map(lambda o: o.hinta(), self._ostokset)
        return sum(hinnat)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for o in self._ostokset:
            if o.tuotteen_nimi() == lisattava.nimi():
                o.muuta_lukumaaraa(1)
                return
        uusi_tuote = Ostos(lisattava)
        self._ostokset.append(uusi_tuote)

    def poista_tuote(self, poistettava: Tuote):
        for o in self._ostokset:
            if o.tuotteen_nimi() == poistettava.nimi():
                o.muuta_lukumaaraa(-1)
                if o.lukumaara() == 0:
                    self._ostokset.remove(o)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
