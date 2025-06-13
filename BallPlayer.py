from Athlete import Athlete


class BallPlayer(Athlete):
    BallPlayer_Amount = 0
    def __init__(self,name,age,country,salary,team_name,jersey_number,endorsement):
        super().__init__(name,age,country,salary)
        self.team_name = team_name
        self.jersey_number = jersey_number
        self.endorsement = endorsement

        BallPlayer.BallPlayer_Amount +=1
    def printStats(self):
        print(str(self.BallPlayer_Amount) + " Ball Player ",end="")

    def printEndorsement(self):
        pass