def karo(width, height, column):

    # Farbwerte:
    a = 255
    b = 255
    c = 0

    d = 0
    e = 0
    f = 255

    for x in range(0, width, +2):
        for y in range(0, height, +2):
            y3 = y * 3
            column[x][y3] = a
            column[x][y3 + 1] = b
            column[x][y3 + 2] = c
            column[x][y3 + 3] = d
            column[x][y3 + 4] = e
            column[x][y3 + 5] = f

            column[x+1][y3] = d
            column[x+1][y3 + 1] = e
            column[x+1][y3 + 2] = f
            column[x+1][y3 + 3] = a
            column[x+1][y3 + 4] = b
            column[x+1][y3 + 5] = c

    return column

