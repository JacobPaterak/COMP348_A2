from Athlete import Athlete


def safe_str(value):
    if value == "null":
        return ""
    else:
        return str(value)


class HockeyPlayer(Athlete):
    Amount_Of_Hockey = 0
    def __init__(self,name,age,country,salary,HockeyPosition,goals_scored,stick_brand,skates_size):
        super().__init__(name,age,country,salary)
        self.HockeyPosition = HockeyPosition
        self.goals_scored = goals_scored
        self.stick_brand = stick_brand
        self.skates_size = skates_size

        HockeyPlayer.Amount_Of_Hockey +=1
    def printStats(self):
        print(str(HockeyPlayer.Amount_Of_Hockey) + " Hockey Players")

    def getG(self):
        return self.goals_scored
    def getE(self):
        pass

    def stringify(self):
        return f"HockeyPlayer:{safe_str(self.name)},{safe_str(self.age)},{safe_str(self.country)},{safe_str(self.salary)},{safe_str(self.HockeyPosition)},{safe_str(self.goals_scored)},{safe_str(self.stick_brand)},{safe_str(self.skates_size)}"
    def parse(self,text):
        elements = []

        for element in text:
            el = element.strip()
            if el == "":
                elements.append("null")
            else:
                elements.append(el)
        while(len(elements) != 8):
            elements.append("null")
        return HockeyPlayer(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5],elements[6],elements[7])