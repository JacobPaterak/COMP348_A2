
class Athlete:
    Amount_Of_Athletes = 0
    def __init__(self,name,age = "null",country = "null",salary = "null"):
        self.name = name
        self.age = age
        self.country = country
        self.salary = salary

        Athlete.Amount_Of_Athletes +=1
    def printStats(self):
        pass
    def printEndorsement(self):
        pass



