#Chapter 3: Quiz Games and If Statements: Lab 3: Create-a-Quiz

#3.1

score = 0

print("Frage 1: ")
answer_one = int(input("Was ergbit 4*5? "))

if answer_one == 20:
    print("Correct")
    score +=1
else:
    print("False")
print()

print("Frage 2: ")
answer_two = int(input("In welchem Jahr war der erste Corona-Lockdown in Deutschland? "))
if answer_two == 2020:
    print("Correct")
    score +=1
print()

print("Frage 3: ")
print("Welcher Name hat mehr Vokale? ")
print("Anwort A: Peter")
print("Antwort B: Julia")
print("Antwort C: Manfred")

answer_three = input("Was ist deine Antwort? ")
if answer_three == "B" or answer_three == "b" or answer_three == "Julia" or answer_three == "julia":
    print("Correct")
    score +=1
else:
    print("False")
print()

print("Frage 4: ")
answer_four = input("In welcher Sprache ist das Programm geschrieben?")
if answer_four == "Python" or answer_four == "python":
    print("Correct")
    score +=1
else:
    print("False")
print()

print("Frage 5: ")
answer_five = int(input("Wie viele Fragen hast du bis hier hin richtig beantwortet? "))
if answer_five == score:
    print("Correct")
    score +=1
else:
    print("False")
print()

percent = 100/5 *score
print("Du hast ", score, "/5 Fragen richtig beantwortet, dass sind ", percent,"%")
