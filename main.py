#main wir vom raspi gestartet wenn eingetragen in ect. Von hier aus kann/wird alles ausgeführt


from sys import platform                #um zu checken ob auf Windows oder aufm Raspi, aufm raspi wird die LED`S ausgegeben aufm Windoof ein Fenster.
import time
import hardware
import windows
import muster1
if platform == "linux" or platform == "linux2":
    import board
    import neopixel
    import LED_Test

width = 100
height = 36

if platform == "linux" or platform == "linux2":
    pixels = neopixel.NeoPixel(board.D18, 7, brightness=0.2, auto_write=False,pixel_order = neopixel.GRB)


def main():

    if platform == "linux" or platform == "linux2":

        LED_Test.LEDTest(1, pixels)

    column = [0 for x in range(width)]          #erstellen vom Array
    for x in range(width):
        column[x] = bytearray(height * 3 + 1)



    #wenn der Knopf dann Bild Umwandeln und speichern
    column = muster1.saw(width ,height, column)
    #wenn Muster dann Muster speichern
    #gespeichert wir in der column[x], x ist die breite. Für jede x ist ein Array, dieses ist höhe*3 groß sodas 0,1,2 Grün Rot Blau werte für ersten pixel sind. 3,4,5 für den nächsten usw.




    #Variablen wie "Reihendauer" einlesen

    #Anzeigen auf Knopfdruck

    if platform == "linux" or platform == "linux2":
        hardware.LEDAnzeigen(column, width, height, pixels)

    elif platform == "win32":

        windows.muster_anzeigen(column, width, height)


main()





