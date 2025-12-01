class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def same_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def advatage_or_win(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def get_written_score(self, points):
        if points == 0:
            return "Love"
        if points == 1:
            return "Fifteen"
        if points == 2:
            return "Thirty"
        if points == 3:
            return "Forty"
        
    def parse_score(self,):
        score_string = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score_string = score_string + "-"
                temp_score = self.m_score2

            score_string += self.get_written_score(temp_score)

        return score_string

    def get_score(self):
        score = ""
    
        if self.m_score1 == self.m_score2:
            score = self.same_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.advatage_or_win()
        else:
            score = self.parse_score()

        return score
