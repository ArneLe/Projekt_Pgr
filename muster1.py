#Schräge
def saw(width, height, column, f1r, f1g, f1b, f2r, f2g, f2b, f):
    h = 0
    w = 0
    for x in range(width):
        for y in range(height):
            y3 = y * 3
            farbe = wheel(x + y)

            if x < height:
                if y == x:
                    column[x][y3] = clamp(f1g + (f*int((farbe[0]))))
                    column[x][y3 + 1] = clamp(f1r + (f*int((farbe[1]))))
                    column[x][y3 + 2] = clamp(f1b + (f*int((farbe[2]))))
                else:
                    column[x][y3] = clamp(f2g + (f*int((farbe[0]))))
                    column[x][y3 + 1] = clamp(f2r + (f*int((farbe[1]))))
                    column[x][y3 + 2] = clamp(f2b + (f*int((farbe[2]))))

            elif x >= height and h%2 == 1:
                if height - y == x-h*height:
                    column[x][y3] = clamp(f1g + (f*int((farbe[0]))))
                    column[x][y3 + 1] = clamp(f1r + (f*int((farbe[1]))))
                    column[x][y3 + 2] = clamp(f1b + (f*int((farbe[2]))))
                else:
                    column[x][y3] = clamp(f2g + (f*int((farbe[0]))))
                    column[x][y3 + 1] = clamp(f2r + (f*int((farbe[1]))))
                    column[x][y3 + 2] = clamp(f2b + (f*int((farbe[2]))))

            elif x >= height and h % 2 == 0:
                if y == x - h * height:
                    column[x][y3] = clamp(f1g + (f*int((farbe[0]))))
                    column[x][y3 + 1] = clamp(f1r + (f*int((farbe[1]))))
                    column[x][y3 + 2] = clamp(f1b + (f*int((farbe[2]))))
                else:
                    column[x][y3] = clamp(f2g + (f*int((farbe[0]))))
                    column[x][y3 + 1] = clamp(f2r + (f*int((farbe[1]))))
                    column[x][y3 + 2] = clamp(f2b + (f*int((farbe[2]))))
        w = w + 1
        if w == height:
            w = 0
            h = h +1


    return column


#Karomuster
def karo(width, height, column, f1r, f1g, f1b, f2r, f2g, f2b, f):


    for x in range(0, width, +2):
        for y in range(0, height, +2):
            y3 = y * 3
            farbe = wheel(x + y)
            column[x][y3] = clamp(f1g + (f*int((farbe[0]))))
            column[x][y3 + 1] = clamp(f1r + (f*int((farbe[1]))))
            column[x][y3 + 2] = clamp(f1b + (f*int((farbe[2]))))
            column[x][y3 + 3] = clamp(f2g + (f*int((farbe[0]))))
            column[x][y3 + 4] = clamp(f2r + (f*int((farbe[1]))))
            column[x][y3 + 5] = clamp(f2b + (f*int((farbe[2]))))

            column[x+1][y3] = clamp(f2g + (f*int((farbe[0]))))
            column[x+1][y3 + 1] = clamp(f2r + (f*int((farbe[1]))))
            column[x+1][y3 + 2] = clamp(f2b + (f*int((farbe[2]))))
            column[x+1][y3 + 3] = clamp(f1g + (f*int((farbe[0]))))
            column[x+1][y3 + 4] = clamp(f1r + (f*int((farbe[1]))))
            column[x+1][y3 + 5] = clamp(f1b + (f*int((farbe[2]))))

    return column



#waagerechte Streifen
def waagerecht(width, height, column, f1r, f1g, f1b, f2r, f2g, f2b,f):

    for x in range(0, width, +1):
        for y in range(0, height, +2):
            y3 = y * 3
            farbe = wheel(x+y)
            column[x][y3] = clamp(f1g + (f*int((farbe[0]))))
            column[x][y3 + 1] = clamp(f1r + (f*int((farbe[1]))))
            column[x][y3 + 2] = clamp(f1b + (f*int((farbe[2]))))
            column[x][y3 + 3] = clamp(f2g + (f*int((farbe[0]))))
            column[x][y3 + 4] = clamp(f2r + (f*int((farbe[1]))))
            column[x][y3 + 5] = clamp(f2b + (f*int((farbe[2]))))
        print(farbe)

    return column


#senkrechte Streifen
def senkrecht(width, height, column, f1r, f1g, f1b, f2r, f2g, f2b, f):

    for x in range(0, width, +2):
        for y in range(0, height, +2):
            y3 = y * 3
            farbe = wheel(x + y)
            column[x][y3] = clamp(f1g + (f*int((farbe[0]))))
            column[x][y3 + 1] = clamp(f1r + (f*int((farbe[1]))))
            column[x][y3 + 2] = clamp(f1b + (f*int((farbe[2]))))
            column[x][y3 + 3] = clamp(f1g + (f*int((farbe[0]))))
            column[x][y3 + 4] = clamp(f1r + (f*int((farbe[1]))))
            column[x][y3 + 5] = clamp(f1b + (f*int((farbe[2]))))

            column[x+1][y3] = clamp(f2g + (f*int((farbe[0]))))
            column[x+1][y3 + 1] = clamp(f2r + (f*int((farbe[1]))))
            column[x+1][y3 + 2] = clamp(f2b + (f*int((farbe[2]))))
            column[x+1][y3 + 3] = clamp(f2g + (f*int((farbe[0]))))
            column[x+1][y3 + 4] = clamp(f2r + (f*int((farbe[1]))))
            column[x+1][y3 + 5] = clamp(f2b + (f*int((farbe[2]))))


    return column


#Regenbogen Muster
def regenbogen(width, height, column):

    for x in range(0, width, +1):
        for y in range(0, height, +1):
            farbe = wheel(y+x)
            y3 = y * 3
            column[x][y3] = farbe[0]
            column[x][y3 + 1] = farbe[1]
            column[x][y3 + 2] = farbe[2]
    print (wheel(y+x))

    return column

"Hier wird eine Wert von 0 bis 255 in einen 3Stelligen Farbwert umgewandelt, wie ein Regenbogen"


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = b = g = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)

def clamp(n):
    return max(min(255, n), 0)