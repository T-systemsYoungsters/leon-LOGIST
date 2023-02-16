#Chapter 4: Guessing Games with Random Numbers and Loops: Lab 4: Camel
import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")


done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
drinks = 4

while not done:

    oasis=random.randrange(20)
    if oasis == 19:
        print("You found an oasis!\n")
        drinks = 4
        camel_tiredness = 0
        thirst = 0
              
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    
    
    user_choice = input("What do you choose? ")
    print()

    if user_choice.upper() == "Q":
        done = True
        print("You Quit the Game")
        
    elif user_choice.upper() == "E":
        print("Miles traveled: ", miles_traveled)
        print("Drinks in canteen: ", drinks)
        print("The natives are ", miles_traveled - natives_traveled, " miles behind you")
        print("###########################################")
        print()
        
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        
        print("The camel is happy")
        print()
        natives_traveled = natives_traveled + random.randrange(7, 20)

    elif user_choice.upper() == "C":
        traveled_new =random.randrange(10,21)
        miles_traveled = miles_traveled + traveled_new
        thirst +=1
        camel_tiredness = camel_tiredness + random.randrange(1,4)
        natives_traveled = natives_traveled + random.randrange(7, 20)
        
        print("You traveled " , traveled_new," miles")
        
        print()
              
    elif user_choice.upper() == "B":
        traveled_new =random.randrange(5,13)
        miles_traveled = miles_traveled + traveled_new
        thirst +=1
        camel_tiredness +=1
        natives_traveled = natives_traveled + random.randrange(7, 20)

        print("You traveled " , traveled_new," miles")
        print()
        
    elif user_choice.upper() == "A":
        if drinks > 0:
            drinks -=1
            thirst = 0
        else:
            print("You don´t have any drinks :/")
            print()
    else:
        print("##########")
        print("Wrong input")
        print("##########")
        print()

    if miles_traveled >= 200 and done == False:
        print("You won!")
        done = True
    
    if thirst > 6 and done == False:
        print("You died of thirst!")
        done = True
        
    elif thirst > 4 and done == False:
        print("You are thirsty")
        print()
        
    if camel_tiredness > 8 and done == False:
        print("Your camel died of tiredness!")
        done = True
        
    elif camel_tiredness > 5 and done == False:
        print("Your  camel is tired")
        print()

    if natives_traveled >= miles_traveled and done == False:
        done = True
        
    elif natives_traveled >= (miles_traveled -15) and done == False:
        print("The natives are getting close!")
        print()

    
        
