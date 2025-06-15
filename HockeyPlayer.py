from Athlete import Athlete
from HockeyPosition import HockeyPosition

def safe_str(value):
    if value == "null":
        return ""
    else:
        return str(value)


class HockeyPlayer(Athlete):
    Amount_Of_Hockey = 0
    def __init__(self,name,age,country,salary,HockeyPositionVal,goals_scored,stick_brand,skates_size):
        super().__init__(name,age,country,salary)
        if isinstance(HockeyPositionVal, str):
            try:
                self.HockeyPosition = HockeyPosition[HockeyPositionVal]  # uses enum member name
            except KeyError:
                self.HockeyPosition = HockeyPosition.Forward  # default
        elif isinstance(HockeyPositionVal, HockeyPosition):
            self.HockeyPosition = HockeyPositionVal
        self.goals_scored = goals_scored
        self.stick_brand = stick_brand
        self.skates_size = skates_size

        HockeyPlayer.Amount_Of_Hockey +=1
        print(
            f"Hockey Player '{self.name}', {self.age} created; total # of hockey players {HockeyPlayer.Amount_Of_Hockey}.")
    def printStats(self):
        print( self.stringify())

    def getG(self):
        return self.goals_scored
    def getE(self):
        pass

    def stringify(self):
        return f"HockeyPlayer:{safe_str(self.name)},{safe_str(self.age)},{safe_str(self.country)},{safe_str(self.salary)},{safe_str(self.HockeyPosition.value)},{safe_str(self.goals_scored)},{safe_str(self.stick_brand)},{safe_str(self.skates_size)}"
    @staticmethod
    def parse(text):
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