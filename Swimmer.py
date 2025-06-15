from Athlete import Athlete


def safe_str(value):
    if value == "null":
        return ""
    else:
        return str(value)


class Swimmer(Athlete):
    Swimmer_Amount = 0
    def __init__(self,name,age,stroke_style,country,salary,personal_best_time):
        super().__init__(name,age,country,salary)
        self.stroke_style = stroke_style
        self.personal_best_time = personal_best_time

        Swimmer.Swimmer_Amount +=1
        print(f"Swimmer '{self.name}', {self.age} created; total # of swimmers {Swimmer.Swimmer_Amount}.")
    def printStats(self):
        print(str(self.Swimmer_Amount) + " Swimmers")
    def printStats(self):
        print(self.stringify())
    def stringify(self):
        return f"Swimmer: {safe_str(self.name)},{safe_str(self.age)},{safe_str(self.stroke_style)},{safe_str(self.country)},{safe_str(self.salary)},{safe_str(self.personal_best_time)}"
    def getE(self):
        pass

    @staticmethod
    def parse(text):
        elements = []

        for element in text:
            el = element.strip()

            if el == "":
                elements.append("null")
            else:
                elements.append(el)
        while (len(elements) < 6):
            elements.append("null")
        return Swimmer(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5])