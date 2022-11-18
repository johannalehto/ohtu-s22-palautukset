from datetime import datetime

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, country: str):
        print(f'Players from {country} {datetime.now()} \n')

        filtered_players = list(filter(lambda player : player.nationality == country, self.players))

        return sorted(filtered_players, key=lambda player : player.points, reverse=True)
