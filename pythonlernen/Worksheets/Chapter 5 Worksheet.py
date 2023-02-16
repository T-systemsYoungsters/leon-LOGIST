import pygame
pygame.init()



#1 Das Computerkoordinatensystem hat den Ursprung links oben mit (0,0). Die y-Achse die theoretisch vom Ursprung aus nach unten geht hat dennoch positive Werte

#2 import pygame und pygame.init()

#3 spiegelt die RGB farben wieder : (Red, Green, Blue)

#4 wenn die Farbe seinen Wert im Laufe des Programms nicht verändert also bei einer konstanten

#5 Festlegung der Größe des Fensters

#6 prüft Eingaben des nutzers

#7 Festlegung wie oft der Bildschirm aktualisiert wird

#8 screen sagt, falls mehrere Fenster vorhanden, auf welchem gemalt werden soll
    #[0, 0] Start x und y Koordinate [100,100] End x und y Koordinate
    # beschreibt die Liniendicke

#9
"""
for x in range(0,100,20):
    pygame.draw.line(screen, color, [x, 0][x, 200], 2)
    pygame.display.flip()
"""

#10 Das Rechteck wird komplett mit Farbe ausgefüllt

#11 20,20 sind die linke obere  ecke des rechtecks, in der sich die ellipse befindet.
    #100 ist die Höhe/Breite und 250 die Länge

#12 pi muss als variable definiert werden

#13 Festlegen welche Font und font größe verwendet werden soll, dann einen "Stempel"
    #generieren, auf dem der Text steht und schließlich diesen Stempel auf das Fenster "abdrücken"

#14 sofern sich die Font nicht ändert kann das außerhalb der loop sein, da so weniger Leistung gebraucht wird

#15 50,100 : 0,200 : 200,200 : 100,50 sind die jeweiligen Eckkoordinaten

#16 flipt souzusagen den screen und zeigt auf dem Fenster was gemalt wurde

#17 schließt das Fenster

#18
"""
pygame.draw.circle(
    screen,             # Surface to draw on
    [100, 100, 100],    # Color in RGB Fashion
    [100, 100],         # Center
    20,                 # Radius
    )
"""
