# main wir vom raspi gestartet wenn eingetragen in ect. Von hier aus kann/wird alles ausgefuehrt


from sys import platform  # um zu checken ob auf Windows oder aufm Raspi, aufm raspi wird die LED`S ausgegeben aufm Windoof ein Fenster.
import time
import hardware
import muster1
import muster2
if platform == "linux" or platform == "linux2":
    import board
    import neopixel
    import LED_Test
else:
    import windows

width = 100
height = 34

if platform == "linux" or platform == "linux2":
    pixels = neopixel.NeoPixel(board.D18, 34, brightness=0.2, auto_write=False,pixel_order = neopixel.GRB)


def main():

    if platform == "linux" or platform == "linux2":

        LED_Test.LEDTest(1, pixels)

    column = [0 for x in range(width)]          #erstellen vom Array
    for x in range(width):
        column[x] = bytearray(height * 3 + 1)



    # wenn der Knopf dann Bild Umwandeln und speichern

    #column = muster1.saw(width, height, column)
    column = muster2.karo(width, height, column)

    # wenn Muster dann Muster speichern





    #Variablen wie "Reihendauer" einlesen

    #Anzeigen auf Knopfdruck

    if platform == "linux" or platform == "linux2":
        hardware.LEDAnzeigen(column, width, height, pixels)

    elif platform == "win32":

        windows.muster_anzeigen(column, width, height)


main()





