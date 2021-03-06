import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipä)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_oikein(self):
        maito = Tuote("Maito", 3)
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipä)
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_oikein(self):
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(leipä)
        self.kori.lisaa_tuote(leipä)
        self.assertEqual(self.kori.hinta(), 10)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
 
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.hinta(), 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipä)
 
        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(leipä)
        self.kori.lisaa_tuote(leipä)
        
        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_nimi_ja_lukumäärä_täsmäävät(self):
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(leipä)
        self.kori.lisaa_tuote(leipä)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Leipä")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_poistaminen_toimii_kahdella_samalla_tuotteella(self):
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(leipä)
        self.kori.lisaa_tuote(leipä)
        self.kori.poista_tuote(leipä)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_viimeisen_tuotteen_poistaminen_tyhjentää_korin(self):
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(leipä)
        self.kori.poista_tuote(leipä)

        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 0)

    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        leipä = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipä)
        self.kori.tyhjenna()

        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 0)