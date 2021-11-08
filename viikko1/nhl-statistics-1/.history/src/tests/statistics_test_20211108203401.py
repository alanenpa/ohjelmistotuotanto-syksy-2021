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

    def test_search_works(self):
        result = self.statistics.search("Kurri")

        self.assertAlmostEqual(result.name, "Kurri")
        self.assertAlmostEqual(result.team, "EDM")
        self.assertEqual(result.goals, 37)
        self.assertEqual(result.assists, 53)

    def test_search_returns_none(self):
        result = self.statistics.search("Xyz")

        self.assertIsNone(result)

    def test_correct_players_with_team_method(self):
        playerlist = self.statistics.team("EDM")

        self.assertAlmostEqual(playerlist[0].name, "Semenko")
        self.assertEqual(len(playerlist), 12)
        print(playerlist[0], playerlist[1], playerlist[2])
