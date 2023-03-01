1. Eine Klasse enthät mehrere Daten, wie z.B. Attribute und Methoden. Ein Objekt über eine Klasse erstellt werden bzw. Teil einer Klasse sein, dadruch hat das Objekt die selben Methoden und Attribute wie die Klasse. <br>

2. Eine Methode ist im Prinzip eine Funktion innerhalb einer Klasse, damit wird einem Objekt, welches Teil einer Klasse ist verschiedene Funtkionen zugewiesen, welche ausgeführt werden können. <br>

3. 
````python
class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

my_dog = Dog()
m_dog.age = 4
my_dog.name = "Big Mac"
my_dog.weight = 21.06
````
<br>

4. 
````python 
class Person():
    def __init__(self):
        self.name = ""
        self.cell_phone = ""
        self.email = ""

my_dude = Person()
my_dude.name = "Manfred"
my_dude.cell_phone = "0152 08461374"
my_dude.email = "manfred.muster@telekom.de
his_dude = Person()
his_dude.name = "Boris"
his_dude.cell_phone = "0152 74385673"
his_dude.email = "boris.boris@telekom.de"
````
<br>

5. 
````python
class  Bird():
    def __init_(self):
        self.color = ""
        self.name = ""
        self.breed = ""

my_bird = Bird()
my_bird.color = "green"
my_bird.name = "Sunny"
my_bird.breed = "Sun Conure"
````
<br>

6. 
````python
class Character():
    def __init__(self)
        self.x_coord = 
        self.y_coord = 
        self.name = ""
        self.strength =
````
<br>

7. 
````python
class Person():
    def __init__(self):
        self.name = ""
        self.money = 
 
nancy = Person()
name = "Nancy"
money = 100
````
Es muss nancy.name und nancy.money sein <br>


8. 
````python
class Person():
    def __init__(self):
        self.name = ""
        self.money = 
 
bob = Person()
print(bob.name, "has", money, "dollars.")
````
Bob bekommt keinen Namen und 0 Money. Vor dem Print muss bob.name = bob und bob.money = xy. Zusätzlich muss im print bob.money stehen.<br>

9. wie in aufgabe 8

10. Customer has a Address<br>
    Person has a Bank Account <br>
    Customer is a Person <br>
    Mortgage account is a Bank Account<br>
    <br>

11. 
````python
class Product():
    def __init__(self):
        self.product_number = ""
        self.product_name = ""
    
class Cola(Product):
    def __init__(self):
        self.taste = ""
        self.size = ""
````
Cola is a Product
 <br>

12. 
````python
class Poduct():
    def __init__(self):
        self.name = ""
````
Product has a name
<br>

13. Man kann es in einer Liste speichern
<br>

14. 
````python
class Animal():
    def __init__(self):
        self.name = ""
        print("An animal has been born.")

    def eat(self):
        print("Munch munch")
    def make_noise(self):
        print("Grrr says ", self.name)

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("A cat has been born.")
    def make_noise(self):
        print("Meow says ", self.name)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("A dog has been born.")
    def make_noise(self):
        print("Bark says",self.name)

my_cat = Cat()
my_cat.name = "Tom"
my_cat.eat()
my_cat.make_noise()

my_dog1 = Dog()
my_dog1.name = "Big Mac"
my_dog1.eat()
my_dog1.make_noise()

my_dog2 = Dog()
my_dog2.name = "Alpha"
my_dog2.eat()
my_dog2.make_noise()

my_animal = Animal()
my_animal.name = "Tier"
my_animal.eat()
my_animal.make_noise()
````