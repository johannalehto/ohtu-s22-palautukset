import requests
from player import Player

class PlayerReader:

    @classmethod
    def get_players(cls, url: str):
        players = []
        response = requests.get(url).json()

        for player_dict in response: 
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
            )

            players.append(player)
        
        return players

    def __init__(self, url: str):
        self.url = url
        self.players = self.get_players(self.url)

