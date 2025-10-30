import graphics as gf
import random as rd
rd.seed()

def random_color():
    return gf.color_rgb(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))


win = gf.GraphWin('Janelinha', 300, 200)
raio = 10
segue = True
antes = gf.Point(0, 0)
cores = ['red', 'blue', 'green', 'black']
i = 0


while segue:
    ponto_clique = win.getMouse()
    nova_bola = gf.Circle(ponto_clique, raio)
    nova_bola.setFill(random_color())
    nova_bola.draw(win)
    if ponto_clique.getX() == antes.getX() and ponto_clique.getY() == antes.getY():
        segue = False
    antes = ponto_clique
    i += 1
win.close()
