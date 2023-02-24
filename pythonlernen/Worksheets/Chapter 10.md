1. es werden zwar ein x und y in die Funktion übergeben, werden in der Funktion aber nicht benutzt. Die Funktion zeichnet immer an der selben stelle eine Figur <br>

2. 
````python
pos = pygame.mouse.get_pos()
x= pos[0]
````
<br>

3. Wenn code, der nichts mit event processing zutun hat in der for schleife ist und event processing teilt, kann es, wenn es mehrere events gibt wie key down und key up zu problemen führen, dass eines nicht verarbeitet wird, so kann das Programm mit dem eingabegerät unsynchron werden. <br>

4. wenn keine taste gedrückt wird, soll das objekt sich nicht bewegen, dadurch muss die change variable 0 sein. Wenn eine Taste gedrückt wird wird diese Variable auf einen pos/negativen wert gesetzt um eine Richtungsänderung zu erschaffen, solange die Taste gedrückt wird. Danach wird change wieder auf 0 gesetzt. Wenn man nur per Befehl die Richtung ändern will, also das Objekt bewegt sich die ganze zeit auf x positiv und man will dass es sich jetzt richtung x negativ bewegt funtkioniert die Technik wie beim bouncing rectangle auch<br>

5. Da wir die position der Maus durch eine Funktion bekommen, jedoch kann man die position der Tastatur nicht rausbekommen, da sie sich ja nicht wie der Mauszeiger auf dem Bildschirm befindet <br>

6. (1,1)