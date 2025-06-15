from BallPlayer import BallPlayer


def safe_str(value):
    if value == "null":
        return ""
    else:
        return str(value)


class BasketballPlayer(BallPlayer):
    BasketballPlayer_Amount = 0
    def __init__(self,name,age,team_name,jersey_number,country,salary,endorsement,three_point_pct,rebounds):
        super().__init__(name,age,country,salary,team_name,jersey_number,endorsement)
        self.three_point_pct = three_point_pct
        self.rebounds = rebounds

        BasketballPlayer.BasketballPlayer_Amount +=1
        print(
            f"Basketball Player '{self.name}', {self.age} created; total # of basketball players {BasketballPlayer.BasketballPlayer_Amount}.")
    def printStats(self):
        print(self.stringify())
    def printEndorsement(self):
        if(self.endorsement != "null"):
            print(self.endorsement)
    def getE(self):
        return self.endorsement

    def stringify(self):
        return f"BasketballPlayer:{safe_str(self.name)},{safe_str(self.age)},{safe_str(self.team_name)},{safe_str(self.jersey_number)},{safe_str(self.country)},{safe_str(self.salary)},{safe_str(self.endorsement)},{safe_str(self.three_point_pct)},{safe_str(self.rebounds)}"

    @staticmethod
    def parse( text):
        elements = []

        for element in text:
            el = element.strip()
            if el == "":
                elements.append("null")
            else:
                elements.append(el)
        while (len(elements) != 9):
            elements.append("null")
        return BasketballPlayer(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5],elements[6],elements[7],elements[8])