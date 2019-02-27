

def saw(width, height, column):
    h = 0
    for x in range(width):
        for y in range(height):
            y3 = y * 3

            if h < height:
                if y == x:
                    column[x][y3] = 155
                    column[x][y3 + 1] = 100
                    column[x][y3 + 2] = 100
                else:
                    column[x][y3] = x
                    column[x][y3 + 1] = y
                    column[x][y3 + 2] = 11#
                h = h + 1
            if h >= height:
                if x-h == y:
                    column[x][y3] = 155
                    column[x][y3 + 1] = 100
                    column[x][y3 + 2] = 100
                else:
                    column[x][y3] = x
                    column[x][y3 + 1] = y
                    column[x][y3 + 2] = 11



    return column

