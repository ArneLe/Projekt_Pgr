from graphics import *

def muster_anzeigen(column, width, height):

    win = GraphWin("Muster", width*10, height*10)
    win.setBackground(color_rgb(0, 0, 0))

    for x in range(width):
        for y in range(height):                                                         #height ist fest und gegeben durch die leds
            y3 = y * 3
            rect = Rectangle(Point(x*10,y*10),Point(x*10+10, y*10+10))
            rect.setFill(color_rgb(column[x][y3], column[x][y3 + 1], column[x][y3 + 2]))
            rect.setOutline(color_rgb(column[x][y3], column[x][y3 + 1], column[x][y3 + 2]))
            rect.draw(win)




    win.getMouse()
    win.close()

