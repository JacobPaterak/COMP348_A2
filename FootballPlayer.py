from BallPlayer import BallPlayer


def safe_str(value):
    if value == "null":
        return ""
    else:
        return str(value)


class FootballPlayer(BallPlayer):
    FootballPlayer_Amount = 0
    def __init__(self,name,age,team_name,jersey_number,country,salary,endorsement,touchdowns,passing_yards):
        super().__init__(name,age,country,salary,team_name,jersey_number,endorsement)
        self.touchdowns = touchdowns
        self.passing_yards = passing_yards

        FootballPlayer.FootballPlayer_Amount +=1

    def printStats(self):
        print(str(self.FootballPlayer_Amount) + " Football Players)")
    def printEndorsement(self):
        if(self.endorsement != "null"):
         print(self.endorsement)
    def getE(self):
        return self.endorsement
    def getT(self):
        return self.touchdowns
    def stringify(self):
        return f"FootballPlayer:{safe_str(self.name)},{safe_str(self.age)},{safe_str(self.team_name)},{safe_str(self.jersey_number)},{safe_str(self.country)},{safe_str(self.salary)},{safe_str(self.endorsement)},{safe_str(self.touchdowns)},{safe_str(self.passing_yards)}"
    def parse(self,text):
        elements = []

        for element in text:
            el = element.strip()
            if el == "":
                elements.append("null")
            else:
                elements.append(el)
        while (len(elements) != 9):
            elements.append("null")
        return FootballPlayer(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5],elements[6],elements[7],elements[8])