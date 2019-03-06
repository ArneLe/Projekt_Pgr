zeitderPause = 0.05

import time



def LEDAnzeigen(column, width, height,pixels):
    for x in range(width):
        for y in range(height):                                                         #height ist fest und gegeben durch die leds
            y3 = y * 3
            pixels[y] = (column[x][y3], column[x][y3 + 1], column[x][y3 + 2])
            #pixels[x] = (255, 0, y + 70)

        pixels.show()
        time.sleep(zeitderPause)
