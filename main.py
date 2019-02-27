//main wir vom arduino gestartet wenn eingetragen in ect. Von hier aus kann/wird alles ausgeführt


import time
import board
import neopixel
import LED_Test
import hardware



pixels = neopixel.NeoPixel(board.D18, 7, brightness=0.2, auto_write=False,pixel_order = neopixel.GRB)





LED_Test.LEDTest(1)

//wenn der Knopf dann Bild Umwandeln und speichern

//wenn Muster dann Muster speichern
//gespeichert wir in der column[x], x ist die breite. Für jede x ist ein Array, dieses ist höhe*3 groß sodas 0,1,2 Grün Rot Blau werte für ersten pixel sind. 3,4,5 für den nächsten usw.




//Variablen wie "Reihendauer" einlesen

//Anzeigen auf Knopfdruck

hardware.LEDAnzeigen()
time.sleep(ReihendauerPause?!)



