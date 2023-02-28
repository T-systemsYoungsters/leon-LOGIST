1. Explorer-Optionen -> Ansicht -> Erweiterungen bei bekannten Dateitypen ausblenden: deaktivieren <br>

2.  Photos: .jpg <br>
Graphic art: gif, png <br>
uncompressed images: bmp<br>
Uncompressed sounds: .wav <br>
songs and soundeffects:  mp3,.ogg<br>

3. load außerhalb, blit inenrhalb der Mainloop <br>

4. man kann in einem Bildbearbeitungsprogramm ein jpg als gif abspeichern, jedoch kommt es dabei immer wieder zu Problemen, da beim konvertieren die Bilddatei immer leicht abgeändert wird.n <br>

5. Jpg speichert Bilder mit abgeänderten Farben, um Speicher zu sparen, dadurch bleiben auch beim konvertieren in ein anderes Dateiformat diese Farbunterschiede vorhanden. <br>

6. der erste Song wird außerhalb der mainloop geloaded und play durch pygame.mixer.music.load() und pygame.mixer.music.play(). Zusätzlich wird ein Endevent erstellt, dass dann in der Mainloop der Start für den näschten Song ist: Durch pygame.mixer.music.set_endevent()<br>