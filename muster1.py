

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


def karo(width, height, column, f1r, f1g, f1b, f2r, f2g, f2b):


    for x in range(0, width, +2):
        for y in range(0, height, +2):
            y3 = y * 3
            column[x][y3] = f1g
            column[x][y3 + 1] = f1r
            column[x][y3 + 2] = f1b
            column[x][y3 + 3] = f2g
            column[x][y3 + 4] = f2r
            column[x][y3 + 5] = f2b

            column[x+1][y3] = f2g
            column[x+1][y3 + 1] = f2r
            column[x+1][y3 + 2] = f2b
            column[x+1][y3 + 3] = f1g
            column[x+1][y3 + 4] = f1r
            column[x+1][y3 + 5] = f1b

    return column



def waagerecht(width, height, column, f1r, f1g, f1b, f2r, f2g, f2b):

    for x in range(0, width, +1):
        for y in range(0, height, +2):
            y3 = y * 3
            column[x][y3] = f1g
            column[x][y3 + 1] = f1r
            column[x][y3 + 2] = f1b
            column[x][y3 + 3] = f2g
            column[x][y3 + 4] = f2r
            column[x][y3 + 5] = f2b

    return column





