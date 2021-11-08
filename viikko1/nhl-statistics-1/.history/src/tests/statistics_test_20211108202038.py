import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        result = self.statistics.search("Kurri")
        print(result.name)
        print(result.name)
        print(result.name)
        print(result.name)
        self.assertAlmostEqual(result.name, "Kurri")
        self.assertAlmostEqual(result.team, "EMD")
        self.assertAlmostEqual(result.goals, 37)
        self.assertAlmostEqual(result.assists, 53)
