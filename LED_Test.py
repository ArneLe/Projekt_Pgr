import time

def LEDTest(anzahl, pixels):

    n = 0

    while n < anzahl:

        pixels.fill((255, 0, 0))   #Gruen
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 255, 0))   #Rot
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 255))  #Blau
        pixels.show()
        time.sleep(1)

        pixels[2] = (255, 0,  70)
        pixels.show()
        time.sleep(1)

        pixels[1] = (255, 0,  70)
        pixels.show()
        time.sleep(1)

        pixels[0] = (255, 0,  70)
        pixels.show()
        time.sleep(1)
        n = n + 1

        pixels.fill((0, 0, 0))
        pixels.show()


