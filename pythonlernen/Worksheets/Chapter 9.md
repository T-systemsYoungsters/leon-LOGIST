1. 
````python
for i in range(5):
    print(i + 1)
````
Guess: 1,2,3,4,5 <br>
actual: 1,2,3,4,5<br>

2. 
````python
for i in range(5):
    print(i)
    i = i + 1
````
Guess: 0,1,2,3,4<br>
actual: 0,1,2,3,4<br>

3.
````python
x = 0
for i in range(5):
    x += 1
print(x)
````
Guess: 5 <br>
actual: 5 <br>

4. 
````python
x = 0
for i in range(5):
    for j in range(5):
        x += 1
print(x)
````
Guess: 25<br>
actual: 25<br>

5. 
````python
for i in range(5):
    for j in range(5):
        print(i, j)
````
Guess: 00,01,02,03,04,10,11,12,13,14,20... 43,44<br>
actual: 00,01,02,03,04....43,44<br>

6. 
````python
for i in range(5):
    for j in range(5):
        print("*", end="")
        print()
````
Guess: 25 mal * untereinander<br>
actual: 25 mal * untereinander<br>

7. 
````python
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
````
Guess: * 5x5<br>
actual: * auf ein 5 mal 5 Feld<br>

8. 
````python
for i in range(5):
    for j in range(5):
        print("*", end="")
print()
````
Guess: 25 mal * nebeneinander und zum schluss neue zeile<br>
actual: 25 mal * nebeneinander und zum schluss neue zeile<br>

9. 
````python
# This is supposed to sum a list of numbers
# What is the mistake here?
my_list = [5, 8, 10, 4, 5]
i = 0
for i in my_list:
    i = i + my_list[i]
print(i)
````
Guess: i wird bei jedem durchlauf der forschleife zurückgesetzt auf den eigentlichen i wert, sodass das aufsummierte verloren geht. Eine weitere Variable wie sum wäre zum aufsummieren besser.<br>
actual: Fehler entsteht, da i einen wert bekommt, der nicht in der Liste vorhanden ist.<br>

10. 
````python
for i in range(5):
    x = 0
    for j in range(5):
        x += 1
print(x)
````
Guess: 5<br>
actual: 5<br>

11. 
````python
import random
play_again = "y"
while play_again == "y":
    for i in range(5):
        print(random.randrange(2), end="")
    print()
    play_again = input("Play again? ")
print("Bye!")
````
Guess: zufällige Zahl im dualsystem / zahl nur aus 0 und 1 bestehend<br>
actual: zufällige 0en und 1en<br>

12. 
````python
def f1(x):
    print(x)
y = 3
f1(y)
````
Guess: 3<br>
actual: 3<br>

13. 
````python
def f2(x):
    x = x + 1
    print(x)
y = 3
f2(y)
print(y)
````
Guess: 4<br> 3 <br>

actual: 4<br>
3<br>

14. 
````python
def f3(x):
    x = x + 1
    print(x)
x = 3
f3(x)
print(x)
````
Guess: 4<br
3<br>
actual: 4<br>
3<br>

15. 
````python
def f4(x):
    z = x + 1
    print(z)
x = 3
f4(x)
print(z)
````
Guess: 4, Fehler<br>
actual: 4, Fehler, da z nur in der Funktion existiert<br>

16. 
````python
def foo(x):
    x = x + 1
    print("x=", x)
 
x = 10
print("x=", x)
foo(x)
print("x=", x)
````
Guess: x=10, x=11, x=10<br>
actual: x=10, x=11, x=10<br>

17. 
````python
def f():
    print("f start")
    g()
    h()
    print("f end")
 
def g():
    print("g start")
    h()
    print("g end")
 
def h():
    print("h")
 
f()
````
Guess: f start g start h g end h f end<br>
actual: f start
g start
h
g end
h
f end<br>

18. 
````python
def foo():
    x = 3
    print("foo has been called")
 
x = 10
print("x=", x)
foo()
print("x=", x)
````
Guess: x = 10 foo has been called x=10<br>
actual: x= 10
foo has been called
x= 10<br>

19. 
````python
def a(x):
    print("a", x)
    x = x + 1
    print("a", x)
 
x = 1
print("main", x)
a(x)
print("main", x)
 
def b(y):
    print("b", y[1])
    y[1] = y[1] + 1
    print("b", y[1])
 
y=[123, 5]
print("main", y[1])
b(y)
print("main", y[1])
 
def c(y):
    print("c", y[1])
    y = [101, 102]
    print("c", y[1])
 
y = [123, 5]
print("main", y[1])
c(y)
print("main", y[1])
````
Guess: main 1 a 1 a 2 main 1 main 5 b 5 b 6 main 6 main 5 c 5 c 102 main 5 <br>
actual: main 1
a 1
a 2
main 1
main 5
b 5
b 6
main 6
main 5
c 5
c 102
main 5<br>


<br>
correcting code: <br><br>

1. 
````python
def sum(a, b, c):
    print(a + b + c)
 
sum(10,11,12)
````
<br>

2. 
````python
def increase(x):
    return x + 1
 
x = 10
print("X is", x, " I will now increase x." )
x_inc = increase(x)
print("X is now", x_inc)
````
<br>

3. 
````python
def print_hello():
    print("Hello")
 
print_hello()
````
<br>

4. 
````python
def count_to_ten():
    for i in range(1,10):
        print(i)
 
count_to_ten()
````
<br>

5. 
````python
def sum_list(list):
    sum=0
    for i in list:
        sum += i   
    return sum

list = [45, 2, 10, -5, 100]
print(sum_list(list))
````
<br>

6. 
````python
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))

````
<br>

7. 
````python
def get_user_choice():
    while True:
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
 
        
 
user_command = get_user_choice()
print("You entered:", user_command)
````
<br>

<br>

 For this section, write code that satisfies the following items:

 <br>

 1. 
 ````python
def write_hello():
print("Hello World")
 ````

 2. 
 ````python
 write_hello()
 ````

 3. 
 ````python
 def write_hello_name(name):
    print("Hello ", name)
 ````

4. 
 ````python
 write_hello_name("Mustermann")
 ````

5. 
````python
def multiply(a,b):
    print(a*b)
````

6. 
 ````python
multiply(4,5)
 ````

7. 
````python
def print_n_times(phrase, count)
    for i in range(count):
        print(phrase)

````

8. 
````python
print_n_times("Hello", 5)
````

9. 
````python
def square_number(number):
    number*=number
    return number
````

10. 
````python
print(square_number(2))
````

11. 
````python
def centrifugal_force(m, v,r):
    force = m*(v**2/r)
    return force
````

12. 
````python
print(centrifugal_force(4, 2, 1))
````

13. 
````python
def print_list(list):
    for item in list:
        print(list[item])

list = [1,2,3,4,5]
print_list(list)
````

