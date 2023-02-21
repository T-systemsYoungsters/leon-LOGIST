#Chapter 3: Quiz Games and If Statements:  Lab 3: Create-a-Quiz

#1 Die Klammer zu fehlt in der ersten Zeile

#2
"""
number = int(input("Gib eine Zahl ein: "))

if number > 0:
   print("Die Zahl ist positiv")
elif number < 0:
    print("Die Zahl ist negativ")
else:
    print("Die Zahl ist Null")
"""

#3
"""
number = int(input("Gib eine Zahl ein: "))

if number >= -10 and number <= 10:
    print("Success")
else:
    print("Failure")
"""

#4 Die zwei Antowrtmöglichkeiten werden erst nach der Eingabe des Nutzers angezeigt

#5 die zuweisung von x sollte x=4 sein und nicht mit "=="!  Es sollte x>0 und nicht >= sein, da wenn x=0 die Zahl nicht positiv ist

#6 bei der zuweisung muss dem input ein datentyp gegebenw werden. Es sollte if x==3: sein also mit "==" und am Ende ":"

#7 die variable heißt answer und nicht a, in der If anweisung muss "==" verwendet werden. Hinter dem Else fehlt ein ":" und das else darf nicht eingerückt sein.

#8 verwendet man in der if anweisung ein "and/or" muss man den ganzen Vergleich neu schreiben: x=="Happy" or x=="Glad"

#9
"""
x = 5
y = False
z = True
Buzz

x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print("Fizz")
if z:
    print("Buzz")
"""

#10
"""
True
False
True
False
False
True
False
False
True
False
True

x = 5
y = 10
z = 10
print(x < y)
print(y < z)
print(x == 5)
print(not x == 5)
print(x != 5)
print(not x != 5)
print(x == "5")
print(5 == x + 0.00000000001)
print(x == 5 and y == 10)
print(x == 5 and y == 5)
print(x == 5 or y == 5)
"""

#11
"""
True
False
True
True
True
False
False
True
False -> wäre ein Fehler gewesen

print("3" == "3")
print(" 3" == "3")
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print( (2 == 2) == "True" )
print( (2 == 2) == True )
print(3 < "3")
"""
#12 Die Antwort ist ein String, deshalb muss sie in " stehen also "A" oder "B" oder "C"
#anstatt von else if muss elif stehen. Die Variable Money sollte man vor der If Anweisung deklarieren und 0 setzen 
#in der If anweisung und elif muss zum vergleichen ein == verwendet werden
# Im abschlusssatz könnte man nach dem "with" ein leerzeichen machen, dass die Zahl money nicht direkt an das wort ansetzt

