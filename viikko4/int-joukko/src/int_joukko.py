KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.luvut = [0] * self.kapasiteetti
        print('hei', self.luvut)

        self.määrä = 0

    def kuuluu(self, n):
        on = 0

        for i in range(0, self.määrä):
            if n == self.luvut[i]:
                on = on + 1
                return True

        return False

    def lisaa(self, n):
        if self.määrä == 0:
            self.luvut[0] = n
            self.määrä = self.määrä + 1
            return True

        if not self.kuuluu(n):
            self.luvut[self.määrä] = n
            self.määrä = self.määrä + 1

            if self.määrä % len(self.luvut) == 0:
                taulukko_old = self.luvut
                self.kopioi_taulukko(self.luvut, taulukko_old)
                self.luvut = [0] * (self.määrä + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.luvut)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.määrä):
            if n == self.luvut[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.luvut[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.määrä - 1):
                apu = self.luvut[j]
                self.luvut[j] = self.luvut[j + 1]
                self.luvut[j + 1] = apu

            self.määrä = self.määrä - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.määrä

    def to_int_list(self):
        taulu = [0] * self.määrä

        for i in range(0, len(taulu)):
            taulu[i] = self.luvut[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.määrä == 0:
            return "{}"
        elif self.määrä == 1:
            return "{" + str(self.luvut[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.määrä - 1):
                tuotos = tuotos + str(self.luvut[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.luvut[self.määrä - 1])
            tuotos = tuotos + "}"
            return tuotos
