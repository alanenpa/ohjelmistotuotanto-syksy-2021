class TennisGame:
    deuce = 4

    def __init__(self, name1, name2):
        self.p1_name = name1
        self.p2_name = name2
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.tie_results()
        elif self.p1_score >= TennisGame.deuce or self.p2_score >= TennisGame.deuce:
            return self.deuce_results()
        else:
            return self.results()

    def tie_results(self):
            if self.p1_score == 0:
                return "Love-All"
            elif self.p1_score == 1:
                return "Fifteen-All"
            elif self.p1_score == 2:
                return "Thirty-All"
            elif self.p1_score == 3:
                return "Forty-All"
            else:
                return "Deuce"

    def deuce_results(self):
        comparison = self.p1_score - self.p2_score
        if comparison == 1:
            return "Advantage player1"
        elif comparison == -1:
            return "Advantage player2"
        elif comparison >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def results(self):
        temp_score = 0
        output = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.p1_score
            else:
                output += "-"
                temp_score = self.p2_score

            if temp_score == 0:
                output += "Love"
            elif temp_score == 1:
                output += "Fifteen"
            elif temp_score == 2:
                output += "Thirty"
            elif temp_score == 3:
                output += "Forty"
        
        return output
