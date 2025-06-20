import matplotlib.pyplot as plt
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
Sal_h = 0
Sal_s = 0
Sal_ball = 0
Sal_B = 0
Sal_F = 0
endorsments = {}
goals_Scored = {}
touch_downs = {}
safed = 0
File_Name_2 = "h.txt"
def Menu():
    choice = input("1. Load File \n2. Print Stats \n3. Delete Athlete \n4. Save File \n5. Athlete Info \n6. Display Chart \n7. Exit\n")
    if int(choice) not in range(1,8):
        print("Please enter a valid option\n")
        Menu()
    return choice
def PieChartMenu():
    pie_choice = input("1. Number of Athletes\n2. Number of Athletes specified\n3. Athletes Salaries\n4. Athletes Salaries specified\n5. Endoresments\n")
    if int(pie_choice) not in range(1,6):
        print("Please enter a valid option\n")
        PieChartMenu()
    return pie_choice
file2 = open(File_Name_2,"w")
choice = "1"

while choice !="7":
   choice = Menu()
   if(choice == "1"):

       File_Name = input("Please input the name of the file ")
       file = open(File_Name+".txt","r")

       for line in file:
           typ = line.split(":")
           individual = typ[1].split(",")
           a_counter +=1
           if(typ[0] == "HockeyPlayer"):
               athlete = HockeyPlayer.parse(individual)
               athletes.append(athlete)
               h_counter +=1
           elif(typ[0] == "Swimmer"):
               athlete = Swimmer.parse(individual)
               athletes.append(athlete)
               s_counter += 1
           elif(typ[0] == "BasketballPlayer"):
                athlete = BasketballPlayer.parse(individual)
                athletes.append(athlete)
                b_counter +=1
           elif(typ[0] == "FootballPlayer"):
                athlete = FootballPlayer.parse(individual)
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
       found = False
       for athlete in athletes:
           if athlete.name == name_of_removel:
               athletes.remove(athlete)
               print("The player has been removed")
               safed = 1

               if isinstance(athlete, Swimmer):
                   s_counter -= 1
                   a_counter -= 1
               elif isinstance(athlete, HockeyPlayer):
                   h_counter -= 1
                   a_counter -= 1
               elif isinstance(athlete, BasketballPlayer):
                   b_counter -= 1
                   a_counter -= 1
               elif isinstance(athlete, FootballPlayer):
                   f_counter -=1
                   a_counter -= 1
               found = True
               break
       if not found:
        print("Athlete not found ")
   if (choice == "4"):
       save_choice = input("Do you want to save Y/N:")
       if save_choice == "Y":
            with open(File_Name,"w") as save_file:
                for athlete in athletes:
                    save_file.write(athlete.stringify() + "\n")
            safed = 0
   if (choice == "5"):
       athlete_name = input("Please enter the name of the athlete that you wish to get the info for:")
       for athlete in athletes:
           if athlete.name.strip().lower() ==  athlete_name.strip().lower():
               athlete.printStats()
               if hasattr(athlete,'endorsement') and athlete.endorsement != "null":
                athlete.printEndorsement()
               else:
                   print("They have no endoresments")

   if (choice == "6"):
       pie_choice = PieChartMenu()
       if(pie_choice == "1"):
        sizes = [h_counter,s_counter,(b_counter + f_counter)]
        categories = ["HockeyPlayer","Swimmer","BallPlayer"]
        plt.pie(sizes, labels = categories,autopct='%1.1f%%', startangle=90 )
        plt.title("Number of Athletes")
        plt.axis('equal')
        plt.show()
       if(pie_choice == "2"):
           sizes = [h_counter, s_counter, f_counter,b_counter]
           categories = ["HockeyPlayer", "Swimmer", "FootballPlayer","BasketballPlayer"]
           plt.pie(sizes, labels=categories, autopct='%1.1f%%', startangle=90)
           plt.title("Number of Athletes")
           plt.axis('equal')
           plt.show()
       if(pie_choice == "3"):
           Sal_h = 0
           Sal_B = 0
           Sal_ball = 0
           Sal_F = 0
           Sal_s = 0
           for athlete in athletes:
               if type(athlete) == HockeyPlayer:
                   if athlete.salary != "null":
                    Sal_h += float(athlete.salary)
               if type(athlete) == Swimmer:
                   if athlete.salary != "null":
                    Sal_s += float(athlete.salary)
               if type(athlete) == BasketballPlayer:
                   if athlete.salary != "null":
                    Sal_B += float(athlete.salary)
               if type(athlete) == FootballPlayer:
                   if athlete.salary !="null":
                    Sal_F += float(athlete.salary)
           average_sal = [Sal_h/h_counter, Sal_s/s_counter, (Sal_B + Sal_F)/(b_counter+f_counter)]
           categories = ["HockeyPlayer", "Swimmer","BallPlayer"]
           plt.pie(average_sal, labels=categories, autopct='%1.1f%%', startangle=90)
           plt.title("Athlete Salaries")
           plt.axis('equal')
           plt.show()
       if(pie_choice == "4"):
           Sal_h = 0
           Sal_B = 0
           Sal_ball = 0
           Sal_F = 0
           Sal_s = 0
           for athlete in athletes:
               if type(athlete) == HockeyPlayer:
                   if athlete.salary != "null":
                       Sal_h += float(athlete.salary)
               if type(athlete) == Swimmer:
                   if athlete.salary != "null":
                       Sal_s += float(athlete.salary)
               if type(athlete) == BasketballPlayer:
                   if athlete.salary != "null":
                       Sal_B += float(athlete.salary)
               if type(athlete) == FootballPlayer:
                   if athlete.salary != "null":
                       Sal_F += float(athlete.salary)
           average_sal = [Sal_h / h_counter, Sal_s / s_counter, Sal_B/b_counter,Sal_F/f_counter]
           categories = ["HockeyPlayer", "Swimmer", "BasketballPlayer","FootballPlayer"]
           plt.pie(average_sal, labels=categories, autopct='%1.1f%%', startangle=90)
           plt.title("Athlete Salaries")
           plt.axis('equal')
           plt.show()
       if(pie_choice == "5"):
           endorsments.clear()
           for athlete in athletes:
               if hasattr(athlete,'endorsement'):
                   if(athlete.endorsement != "null"):
                       endorsments[athlete.getE()] = endorsments.get(athlete.getE(), 0) + 1
           e_brands= list(endorsments.keys())
           e_values = list(endorsments.values())
           plt.pie(e_values, labels=e_brands, autopct='%1.1f%%', startangle=90)
           plt.title("Endoresments")
           plt.axis('equal')
           plt.show()


if(choice == "7"):
    if safed == 1:
        option = input("You have yet to save the file so data may be lost do you still want to exit Y/N:")
        if(option == "N"):
            choice = "1"
            Menu()
        else:
            print("Thank you for using our Athlete Managment system")
    else:
        print("Thank you for using our Athlete Managment system")



