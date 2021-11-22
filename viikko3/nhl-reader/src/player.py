class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name}, goals + assists: {self.goals} + {self.assists} = {points}"
