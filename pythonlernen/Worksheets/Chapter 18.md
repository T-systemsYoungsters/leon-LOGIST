1. Exception ist eine "Situation" in der das Programm nicht funktionieren würde, z.B. bei x/y wenn y=0 ist, da durch 0 teilen nicht geht. <br>
Exception Handling ist der Gesamte Prozess<br>
Try block hier wird eine Anweisung "ausprobiert" wenn sie zu einem Fehler führt, wird der Catch block ausgeführt.<br>
Catch block / Exception Block ist der Block in dem steht, was passiert, wenn der try block nicht funktioniert, also ein Fehler auftreten würde<br>
Unhandled exception ist wenn es keinen try/catch block gibt und der Fehler einfach in die Konsole "geworfen" wird
Der Try block "wirft" einen Fehler, wenn die darin enthaltene Anweisung zu einem Fehler führt, diesen Fehler "fängt" der Catch/Exception block und führt die Anweisung die in ihm steht aus. <br>

2. 
````python
user_input_string = input("Enter a number:")
try:
    user_value = int(user_input_string)
except: 
    print("Fehler bei der Konvertierung")
````
<br>

3.  Guess: ABDE error <br>
richtig: A
B
D
E
Traceback (most recent call last):
   line 11, in <module>
    print(a)
NameError: name 'a' is not defined

````python 
x = 5
y = 0
print("A")
try:
    print("B")
    a = x / y
    print("C")
except:
    print("D")
print("E")
print(a)
````
<br>

4. ABCE0.5

````python
x = 5
y = 10
print("A")
try:
    print("B")
    a = x / y
    print("C")
except:
    print("D")
print("E")
print(a)
````