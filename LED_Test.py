import time

def LEDTest(anzahl, pixels):

    n = 0

    while n < anzahl:

        pixels.fill((255, 0, 0))
        pixels[4] = (255, 0, 70)
        pixels[6] = (255, 0,  70)
        pixels[18] = (255, 0,  150)   #Gruen
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 255, 0))   #Rot
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 255))   #Blau
        pixels.show()
        time.sleep(1)
        n = n + 1


