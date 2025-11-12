import graphics as gf
import random as rd
import time
rd.seed()

def random_color():
    return gf.color_rgb(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))

win = gf.GraphWin('Janelinha', 500, 500)

raio = 10
antes = gf.Point(0, 0)
centro = gf.Point(50, 50)

spawnPos = gf.Point(50, 50)
player = gf.Circle(spawnPos, raio)
player.setFill(random_color())
player.draw(win)
spawnPos = gf.Point(200, 50)
nova_bola2 = gf.Circle(spawnPos, raio)
nova_bola2.setFill(random_color())
nova_bola2.draw(win)

aceleracao = 1
velocidadeX = 1
velocidadeY = 0
obstaculos = []

obstaculos.append(nova_bola2)
while True:
    tecla = win.checkKey()
    
    
    if tecla == 'w':
        velocidadeY = velocidadeY - aceleracao
    if tecla == 's':
        velocidadeY = velocidadeY + aceleracao  
    if tecla == 'd':
        velocidadeX = velocidadeX + aceleracao    
    if tecla == 'a':
        velocidadeX = velocidadeX - aceleracao
    if tecla == 'space':
        velocidadeX = 0
        velocidadeY = 0
    playerX = player.getCenter().getX
    playerY = player.getCenter().getY
    for obstaculo in obstaculos:
        obsX = obstaculo.getCenter().getX()
        obsY = obstaculo.getCenter().getY()
        if (playerX + raio > obsX - raio and playerX - raio < obsX + raio) and (playerY + raio > obsY - raio and playerY - raio < obsY + raio):
            velocidadeX = velocidadeX * - 1
            velocidadeY = velocidadeY * - 1

    
    player.move(velocidadeX, velocidadeY)
    

    
    time.sleep(0.0166)
    
win.close()



