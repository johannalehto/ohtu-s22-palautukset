class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def check_tie(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        elif self.player1_score == 3:
            return "Forty-All"
        return "Deuce"

    def check_over_four(self, minus_result: int):
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        return "Win for player2"

    def check_temp_score(self, score: str, temp_score: int):
        if temp_score == 0:
            return score + "Love"
        elif temp_score == 1:
            return score + "Fifteen"
        elif temp_score == 2:
            return score + "Thirty"
        elif temp_score == 3:
            return score + "Forty"
    
    def check_rounds(self, score: str):
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score

            score = self.check_temp_score(score, temp_score)
        return score

    def get_score(self):
        score = ""
        if self.player1_score == self.player2_score:
            return self.check_tie()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self.player2_score
            return self.check_over_four(minus_result)

        return self.check_rounds(score)

