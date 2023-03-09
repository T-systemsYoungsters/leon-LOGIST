1. Der Witz an sich ist eine Rekursion, welche eine Endlosschleife mit sich zieht. Um Rekursion zu verstehen muss man Rekursion verstehen aber um Rekursion zu verstehen muss man Rekursion verstehen....<br>

2. Spiegel 1 spiegelt das Spiegelbild von Spiegel 2, welcher wiederum das Spiegelbild von Spiegel 1, der Spiegel 2 spiegelt, spiegelt.  Spiegel 1 speigelt somit Spiegel 2 der Spiegel 1 spiegelt wie er Spiegel 2 spiegelt... <br>

3. Ein "Kunde" der im Namen eines Unternehmens ein Prdukt in seinem Umfeld bewirbt, kann weitere Leute "anstelllen" diese Produkt zu bewerben, welche wieder andere anstellen können etc. <br>

4. Wenn man auf ein leeres Feld trifft, können durch Rekursion angrenzende Felder geprüft werden und hier bei wieder angrenzende Felder...<br>

5. Man sollte immer EINER Wand folgen, um aus einem labyrinth raus zu kommen, dadruch kann dieser Weg rekursiv dargestellt werden.<br>

6. von Telekom geblockt.<br>

7. 
````python
def f(n):
    if n == 1:
        return 6
    else:
        return 1/2 * f(n-1)+4

for i in range(1,11):
    print(f(i))
````
<br>

8. 
````python
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

for i in range(1,11):
    print(f(i))
````