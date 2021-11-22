class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        playerlist = self.reader.get_players()
        playerlist = filter(lambda x: x.nationality == nationality, playerlist)
        sorted_players = sorted(playerlist, key=lambda x: x.goals + x.assists, reverse=True)
        return sorted_players