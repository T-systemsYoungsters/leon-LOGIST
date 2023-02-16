#Chapter 4: Guessing Games with Random Numbers and Loops: Chapter 04 Worksheet
import random

#1
"""
for i in range(10):
    print("Leon")
print("Done")
"""

#2
"""
for i in range(20):
    print("Red")
    print("Gold")
"""

#3
"""
for i in range(2,100,2):
    print(i)
"""

#4
"""
i=10
while i>=0:
    print(i)
    i-=1
"""

#5 1. Der Input des Nutzers hat keinen datentypen. 2.x wird jedesmal überschrieben und nicht verwendet. Es müsste total= total+x sein
#5 3. es sollte total geprinted werden und nicht x

#6
"""
random_number = random.randrange(1,11)
print(random_number)
"""

#7
"""
random_number = random.random() * 10+1
print(random_number)
"""

#8
"""
count_pos = 0
count_neg = 0
count_zero = 0
number = 0
total = 0

for i in range(7):
    number = int(input("Gib eine Nummer an"))
    total = total + number
    if number > 0:
        count_pos +=1
    elif number < 0:
        count_neg +=1
    else:
        count_zero +=1
    
    
print(total)
print("Anzahl der positive Zahlen: ",count_pos)
print("Anzahl der negative Zahlen: ",count_neg)
print("Anzahl der Zahlen die 0 waren: ",count_zero)
"""

#9
"""
total_head = 0
total_tail = 0

for i in range(50):
    coin = random.randrange(2)


    if coin == 1:
        print("Head!")
        total_head +=1
    else:
        print("Tail!")
        total_tail +=1

print("Anzahl Head: ", total_head, " und Anzahl Tail: ", total_tail)
"""

#10

score_computer = 0
score_user = 0

print("Rock, Paper, Scissors! Wer als erster 3 Punkte hat gewinnt!")
print("1 = Rock,\n2 = Paper,\n3 = Scissors")

while score_computer != 3 and score_user != 3:
    user_choice = int(input("Was wählst du?"))
    computer_choice = random.randrange(1,4)

    if computer_choice == user_choice:
        print("Unentschieden!")
              
    elif computer_choice == 1 and user_choice == 2:
        print("Papier schlägt Stein! \nDu gewinnst!")
        score_user +=1
        
    elif computer_choice == 1 and user_choice ==3:
        print("Stein schlägt Schere! \nDu verlierst!")
        score_computer+=1
        
    elif computer_choice == 2 and user_choice ==1:
        print("Papier schlägt Stein! \nDu verlierst!")
        score_computer +=1

    elif computer_choice == 2 and user_choice ==3:
        print("Schere schlägt Papier! \nDu gewinnst!")
        score_user +=1

    elif computer_choice == 3 and user_choice == 1:
        print("Stein schlägt Schere! \nDu gewinnst!")
        score_user +=1
    elif computer_choice == 3 and user_choice == 2:
        print("Schere schlägt Papier! \nDu verlierst!")
        score_computer +=1
    print(score_user, ":", score_computer)
    print()

if score_user == 3:
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")
    
