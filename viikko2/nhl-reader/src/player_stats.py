
class PlayerStats:
    def __init__(self, data):
        self.data = data

    def get_nationalities(self):
        nationalities = set()
        for player in self.data.players:
            nationalities.add(player.nationality)
        nationalities_str = ", ".join(sorted(nationalities))
        return nationalities_str

    def top_scorers_by_nationality(self, nationality):
        players_sorted = sorted(self.data.players, key=lambda p: p.goals + p.assists, reverse=True)

        palautus = []

        for player in players_sorted:
            if player.nationality == nationality:
                palautus.append(player)
        return palautus
