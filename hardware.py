




def LEDAnzeigen:
    for y in range(height):                                                         //height ist fest und gegeben durch die leds
        y3 = y * 3
        pixels[x] = (column[x][y3], column[x][y3 + 1], column[x][y3 + 2])

    pixels.show()
