import graphics as gf
import random as rd
import time
import math
rd.seed()

def random_color():
    return gf.color_rgb(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))

win = gf.GraphWin('Janelinha', 500, 500)

def circle_collision(body1, body2):
    body1x = body1.getCenter().getX()
    body1y = body1.getCenter().getY()
    body2x = body2.getCenter().getX()
    body2y = body2.getCenter().getY()
    if math.sqrt((body1x - body2x) ** 2 + (body1y - body2y) ** 2) <= body1.getRadius() + body2.getRadius():
        return True
    return False

def circle_wall_collision(circle, wall):
        circleX = circle.getCenter().getX()
        circleY = circle.getCenter().getY()
        horizontal_side = circleX
        vertical_side = circleY
        direction = []
        if circleX < wall.getP1().getX():
            horizontal_side = wall.getP1().getX()
        else:
            if circleX > wall.getP2().getX(): 
                horizontal_side = wall.getP2().getX()

        if circleY < wall.getP1().getY():
            vertical_side = wall.getP1().getY()
        else:
            if circleY > wall.getP2().getY():
                vertical_side = wall.getP2().getY()
        if math.sqrt((circleX - horizontal_side) ** 2 + (circleY - vertical_side) ** 2) <= circle.getRadius():
            return True
        return False


def circle_wall_direction(circle, wall):
    direction = [0, 0]
    circleX = circle.getCenter().getX()
    circleY = circle.getCenter().getY()
    wallP1X = wall.getP1().getX()
    wallP1Y = wall.getP1().getY()
    wallP2X = wall.getP2().getX()
    wallP2Y = wall.getP2().getY()
    if circleX < wallP1X or circleX > wallP2X:
        if circleX < wallP1X:
            if wallP1X - circleX < wallP1Y - circleY:
                direction[0] = -1
                direction[1] = 1
            else:
                direction[0] = -1
                direction[1] = 1
        if circleX > wallP2X:
            if wallP2X - circleX < wallP1Y - circleY:
                direction[0] = 1
                direction[1] = -1
            else:
                direction[0] = 1
                direction[1] = -1
    else:
        direction[0] = -1
        direction[1] = 1
    return direction
        
def generate_wall():
    wall = gf.Rectangle(gf.Point(150, 150), gf.Point(200, 200))
    wall.setFill('black')
    wall.draw(win)
    walls.append(wall)


walls = []
raio = 20
centro = gf.Point(50, 50)
spawnPos = gf.Point(50, 50)
player = gf.Circle(spawnPos, raio)
player.setFill(random_color())
player.draw(win)
spawnPos = gf.Point(200, 50)
# nova_bola2 = gf.Circle(spawnPos, raio)
# nova_bola2.setFill(random_color())
# nova_bola2.draw(win)

aceleracao = 1
velocidadeX = 1
velocidadeY = 0
circles = []
generate_wall()

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
    playerX = player.getCenter().getX()
    playerY = player.getCenter().getY()
    for circle in circles:
        if circle_collision(player, circle):
            velocidadeX = velocidadeX * - 1
            velocidadeY = velocidadeY * - 1
    for wall in walls:
        if circle_wall_collision(player, wall):
            direcao = circle_wall_direction(player, wall)
            velocidadeX = velocidadeX * - 1 * direcao[0]
            velocidadeY = velocidadeY * - 1 * direcao[1]

    player.move(velocidadeX, velocidadeY)
    

    
    time.sleep(0.0166)
    
win.close()



