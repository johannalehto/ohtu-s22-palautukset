import unittest
from statistics import Statistics, SortBy
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
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_by_name(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(str(player), "Semenko EDM 4 + 12 = 16")

    def test_search_by_non_existing(self):
        player = self.statistics.search("Non Existing")
        self.assertIsNone(player)

    def test_team_filter_players(self):
        team_name = self.statistics.team("EDM")
        players_of_team = list(map(lambda player : str(player), team_name))
        comparison = [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124"
        ]
        self.assertEqual(players_of_team, comparison)

    def test_top_sort_players_by_points(self):
        top_players = self.statistics.top(3)
        sorted_players = list(map(lambda player: str(player), top_players))
        comparison = [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98"
        ]
        self.assertEqual(sorted_players, comparison)

    
    def test_top_sort_players_by_goals(self):
        top_players = self.statistics.top(3, SortBy.GOALS)
        sorted_players = list(map(lambda player: str(player), top_players))
        comparison = [
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98",
            "Kurri EDM 37 + 53 = 90"
        ]
        self.assertEqual(sorted_players, comparison)

    def test_top_sort_players_by_assists(self):
        top_players = self.statistics.top(3, SortBy.ASSISTS)
        sorted_players = list(map(lambda player: str(player), top_players))
        comparison = [
            "Gretzky EDM 35 + 89 = 124",
            "Yzerman DET 42 + 56 = 98",
            "Lemieux PIT 45 + 54 = 99"
        ]
        self.assertEqual(sorted_players, comparison)

    

