import time
import board
import neopixel


ORDER = neopixel.GRB  //Die LEDS brachen Grün Rot Blau reinfolge

pixels = neopixel.NeoPixel(board.D18, 7, brightness=0.2, auto_write=False,pixel_order = ORDER)

while True:

    pixels.fill((255, 0, 0)) //Grün
    pixels.show()
    time.sleep(1)


    pixels.fill((0, 255, 0)) //Rot
    pixels.show()
    time.sleep(1)


    pixels.fill((0, 0, 255)) //Blau
    pixels.show()
    time.sleep(1)
