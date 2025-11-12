import graphics as gf

def main():
    win = gf.GraphWin("My Circle", 500, 500)
    while True:
        pos = win.getMouse()
        posX = pos.getX()
        posY = pos.getY()
        c = gf.Circle(gf.Point(posX,posY), 20)
        c.draw(win)
        c2 = gf.Circle(gf.Point(posX + 40, posY), 20)
        c2.draw(win)
        c3 = gf.Oval(gf.Point(posX+ 5, posY + 130), gf.Point(posX + 35, posY+ 10))
        c3.draw(win)
        win.getMouse() # Pause to view result
    win.close()    # Close window when done


main()


