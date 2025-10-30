import graphics as gf

def main():
    win = gf.GraphWin("My Circle", 500, 500)
    linha = gf.Line(gf.Point(50,50), gf.Point(50,200))
    linha2 = gf.Line(gf.Point(100,50), gf.Point(100,200))
    linha3 = gf.Line(gf.Point(0, 100), gf.Point(150,100))
    linha4 = gf.Line(gf.Point(0, 150), gf.Point(150,150))
    linha.draw(win)
    linha2.draw(win)
    linha3.draw(win)
    linha4.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


main()


