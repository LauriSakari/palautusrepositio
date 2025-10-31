import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku_toimii(self):
        haku = self.stats.search("Kurri")

        self.assertIsNotNone(haku)
        self.assertEqual(haku.name, "Kurri")
        
    def test_haku_toimii_jos_pelaajaa_löydy(self):
        haku = self.stats.search("Rantanen")

        self.assertIsNone(haku)

    def test_joukkuehaku_toimii(self):
        haku = self.stats.team("EDM")
        self.assertEqual(len(haku), 3)

# ohjelmassa on bugi, testi on määritelty sen mukaan
    def test_pisteiden_mukaan_järjestäminen_toimii(self):
        haku = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(len(haku), 3)
        self.assertEqual(haku[0].name, "Gretzky")

    def test_maalien_mukaan_järjestäminen_toimii(self):
        haku = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(haku[0].name, "Lemieux")

    def test_syöttöjen_mukaan_järjestäminen_toimii(self):
        haku = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(haku[0].name, "Gretzky")

    def test_sort_by_points_palauttaa_oletuksena_järjestyksen_pisteillä(self):
        haku = self.stats.top(2, 5)
        self.assertEqual(len(haku), 3)
        self.assertEqual(haku[0].name, "Gretzky")
