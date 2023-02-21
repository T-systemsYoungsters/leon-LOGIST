1. Da jedesmal wenn die Loop von vorne beginnt x =50 gesetzt wird, dann x+1 gemacht wird und dann wieder x=50 daruch ist rect_x jedesmal beim zeichnen 50 <br>

2. rect_x = x Position des linken oberen ecks des rechtecks, rect_y = y Position des linken oberen ecks des rechtecks, rect_change_x/ rect_change_y = Veränderung der x/y Koordinate des oberen linken ecks -> daher Richtung und geschwindigkeit des Rechtecks <br>

3. Bei y > 379 <br>

4. Wie oben beschrieben sollte hier auch bei rect_y > 449 die Richtung angepasst werden. In der If Anweisung sollte dann nicht rect_y = rect_y *=-1 sein sondern die Variable, die die Richtung und Geschwindigkeit bestimmt. Ansonsten wird das Rechteck einfach aus dem Screen "teleportiert", da das Rechteck dann von y=450 auf y=-450, was nicht auf dem Screen abgebildet wird, springt.<br>

5. Er kann die jeweiligen Formen mit (x+eine Zahl, die die Figur in Form hält) bewegen. Da jedes "Körperteil um den sekben x-wert verschoben wird, kann er einen festen wert nehmen, der die Körperteile jeweils zusammenhält und diese immer nur um den selben x wert verschieben, so bleibt die Figur ganz und er benutzt nur 1 x. (genauso mit dem y machbar)<br>

6. Je nach dem wie häufig die Loop durchläuft werden z.B. 20 mal in der Sekunde 50 neue X,y werte mit Sternen erzeugt. <br>

7. In dem man eine Liste macht, welche durch eine for schleife verschiedene x und y werte enthält. Diese können dann in die Items als x und y Koordinaten eingesetzt werden.<br>

8. 
````python
print(stars[1][0])
````
<br>

9. Das zweite Beispiel ist die verkürzte Form des ersten Beispiels. Im zweiten Beispiel werden die x und y Koordinaten aus der Liste geholt und direkt in die drawfunktion gepackt. Im ersten Beispiel werden die koordinaten erst in eine x und eine y Koordinate übertragen und dann diese Variablen in die Funktion eingesetzt <br>

10. Der Mittelpunkt bleibt immer fix, damit ist der Anfangspunkt der Linie auch immer der selbe. [145,145]. Der endpunkt der Linie wird bei jedem durchlauf der loop neu berechnet, dabei wird jedesmal der Winkel um 0.03 vergrößert, bis zu dem Ounkt wo der winkel größer 2pi ist, dann wird vom winkel 2pi abgezogen.