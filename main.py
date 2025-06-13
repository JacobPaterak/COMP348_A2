
from Athlete import Athlete
from BallPlayer import BallPlayer
from Swimmer import Swimmer
from HockeyPlayer import HockeyPlayer
from BasketballPlayer import BasketballPlayer
from FootballPlayer import FootballPlayer
athletes = []
a_counter = 0
h_counter = 0
b_counter = 0
f_counter = 0
s_counter = 0
endorsments = {}
goals_Scored = {}
touch_downs = {}
safed = 0
File_Name_2 = "h.txt"
print()
def Menu():
    choice = input("1. Load File \n2. Print Stats \n3. Delete Athlete \n4. Save File \n5. Athlete Info \n6. Display Chart \n7. Exit\n")
    return choice
file2 = open(File_Name_2,"w")



#
# print("Statistics\n" + "-------------------")
# Athlete.printStats(Athlete)
# HockeyPlayer.printStats(HockeyPlayer)
# BallPlayer.printStats(BallPlayer)
# BasketballPlayer.printStats(BasketballPlayer)
# FootballPlayer.printStats(FootballPlayer)
# Swimmer.printStats(Swimmer)






choice = "1"

while choice !="7":
   choice = Menu()
   if(choice == "1"):

       File_Name = input("Please input the name of the file ")
       file = open(File_Name+".txt","r")

       for line in file:
           type = line.split(":")
           individual = type[1].split(",")
           a_counter +=1
           if(type[0] == "HockeyPlayer"):
               athlete = HockeyPlayer.parse(HockeyPlayer,individual)
               athletes.append(athlete)
               h_counter +=1
           elif(type[0] == "Swimmer"):
               athlete = Swimmer.parse(Swimmer,individual)
               athletes.append(athlete)
               s_counter += 1
           elif(type[0] == "BasketballPlayer"):
                athlete = BasketballPlayer.parse(BasketballPlayer,individual)
                athletes.append(athlete)
                b_counter +=1
           elif(type[0] == "FootballPlayer"):
                athlete = FootballPlayer.parse(FootballPlayer,individual)
                athletes.append(athlete)
                f_counter +=1
           else:
               print("Not an option")

   if (choice == "2"):
       endorsments.clear()
       goals_Scored.clear()
       touch_downs.clear()
       print("Statistics:")
       print("-------------------")
       print(str(a_counter) + " Athletes")
       print(str(h_counter) + " Hockey Players")
       print(str(b_counter + f_counter) + " Ball Players (" + str(b_counter) + " Basketball and " + str(f_counter) + " Football Players")
       print(str(s_counter) + " Swimmers\n")
       print("Endoresments:")
       print("-------------------")
       for athlete in athletes:
            if hasattr(athlete,'endorsement'):
                if athlete.getE() != "null":
                    endorsments[athlete.getE()] = endorsments.get(athlete.getE(), 0) + 1
       for brand,amount in sorted(endorsments.items()):
            print(str(brand) + " (" +  str(amount) + ")")
       print("\nGoals Scored:")
       print("-------------------")
       for athlete in athletes:
           if hasattr(athlete,'goals_scored'):
               if athlete.getG() != "null":
                   goals_Scored[athlete.name] = int(athlete.getG())
       for name,num_goals in sorted(goals_Scored.items(), key=lambda item: item[1], reverse = True):
           print(str(num_goals)+ " " + str(name))
       print("\nTouchdowns:")
       print("-------------------")
       for athlete in athletes:
           if hasattr(athlete,'touchdowns'):
               if athlete.getT() != "null":
                touch_downs[athlete.name] = int(athlete.getT())
       for name,num_touch_downs in sorted(touch_downs.items(),key =lambda item: item[1],reverse = True):
            print(str(num_touch_downs) + " " + name)
       print("\n\n")
   if (choice == "3"):
       name_of_removel = input("Please input the name of the Athlete you wish to remove:")
       for athlete in athletes:
           if athlete.name == name_of_removel:
               athletes.remove(athlete)
               print("The player has been removed")
               safed = 1
   #  Need to make sure that no 2 athlets have the same name

   if (choice == "4"):
       save_choice = input("Do you want to save Y/N:")
       if save_choice == "Y":
            for athlete in athletes:
                file.write(athlete.stringify() + "\n")
            file.close()
            file.open()
            safed = 0
   if (choice == "5"):
       athlete_name = input("Please enter the name of the athlete that you wish to get the info for:")
       for athlete in athletes:
           if athlete.name == athlete_name:
               athlete.printStats()
               athlete.printEndorsement()
       print("Hello5")
   if (choice == "6"):
       print("Hello6")
if(choice == "7"):
    if safed == 1:
        option = input("You have yet to save the file so data may be lost do you still want to exit Y/N:")
        if(option == "Y"):
            choice = "1"
            Menu()
        else:
            print("Thank you for using our Athlete Managment system")
    else:
        print("Thank you for using our Athlete Managment system")



