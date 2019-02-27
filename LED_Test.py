

def LEDTest(int anzahl):

n = 0

while n< anzahl:

    pixels.fill((255, 0, 0)) // Grün
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0)) // Rot
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255)) // Blau
    pixels.show()
    time.sleep(1)


