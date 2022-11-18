class Player:
    def __init__(self, name: str, nationality: str, team: str, goals: int, assists: int):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = goals + assists   

    def __str__(self):
        return f'{self.name:20}{self.team:4}{self.goals:2} + {self.assists:2} = {self.points:2}'
