




def LEDAnzeigen(column, width, height):
    for x in range(width):
        for y in range(height):                                                         #height ist fest und gegeben durch die leds
            y3 = y * 3
            pixels[x] = (column[x][y3], column[x][y3 + 1], column[x][y3 + 2])

        pixels.show()

    time.sleep(zeitderPause)




