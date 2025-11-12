import graphics as gf
import random as rd
import time
rd.seed()


def random_color():
    return gf.color_rgb(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))


def generateBoard():
    for i in range(board_size + 1):
        for j in range(board_size + 1):
            tile = gf.Rectangle(gf.Point(90 + i * 20, 90 + j * 20), gf.Point(90 + (i + 1) * 20, 90 + (j + 1) * 20))
            # condicao que faz o padrao de xadrez
            if (i + j) % 2 == 0:
                tile.setFill(gf.color_rgb(220, 220, 220))
            else:
                tile.setFill(gf.color_rgb(190, 190, 190))
            tile.setOutline('')
            tile.draw(win)


def detect_collision(pos1, pos2):
    if pos1.getX() == pos2.getX() and pos1.getY() == pos2.getY():
        return True
    return False


def detect_out_of_bounds(pos):
    if pos.getX() < boardLimits[0] or pos.getX() > boardLimits[1] or pos.getY() < boardLimits[0] or pos.getY() > boardLimits[1]:
        return True
    return False


def generate_snake():
    grow(gf.Point(200, 200), 'lightgreen')
    for i in range(1, 5):
        grow(gf.Point(200 - i * 20, 200), 'green')


# aumenta o tamanho da cobrinha em 1
def grow(pos, color):
    segment = gf.Circle(pos, radius)
    segment.setFill(color)
    segment.draw(win)
    segments.append(segment)


def spawnApple():
    spawnPos = gf.Point(300, 300) 
    apple = gf.Circle(spawnPos, radius)
    apple.setFill('red')
    apple.draw(win)
    return apple


# troca a posição da maçã quando ela é comida
def changeApplePos():
    while True:
        spawn_x = roundCoordinate(rd.randint(boardLimits[0], boardLimits[1]))
        spawn_y = roundCoordinate(rd.randint(boardLimits[0], boardLimits[1]))
        if isApplePosValid(gf.Point(spawn_x, spawn_y)):
            break
    apple.move(spawn_x - apple.getCenter().getX(), spawn_y - apple.getCenter().getY())
    

def isApplePosValid(pos):
    valid_pos = True
    for segment in segments:
        if detect_collision(pos, segment.getCenter()):
            valid_pos = False
            print("a")
    return valid_pos


# arredonda a coordenada para um multiplo do raio * 2
def roundCoordinate(coordinate):
    round_way = 1
    if coordinate % move_distance < 10:
        round_way = - 1
    while coordinate % move_distance != 0:
        coordinate += round_way
    return coordinate


win = gf.GraphWin('Janelinha', 500, 500)

# algumas variaveis importantes...
segments = []
board_size = 16
radius = 10
move_distance = radius * 2 # ten que ser o dobro do raio
boardLimits = [100, 100 + board_size * move_distance]
move_direction = [1, 0] # direcao inicial da cobra
generateBoard()
apple = spawnApple()
generate_snake()
game_ended = False

# loop principal do jogo
while game_ended == False:
    tecla = win.checkKey()
    
    # posicao inicial da cabeça da cobra
    pos_antiga_x = segments[0].getCenter().getX()
    pos_antiga_y = segments[0].getCenter().getY()

    # altera a direção 
    if tecla == 'w' and move_direction != [0, 1]:
        move_direction = [0, -1]
    if tecla == 's' and move_direction != [0, -1]:
        move_direction = [0, 1]

    if tecla == 'd' and move_direction != [-1, 0]:
        move_direction = [1, 0]

    if tecla == 'a' and move_direction != [1, 0]:
        move_direction = [-1, 0]

    # move a cabeça com base na tecla clicada
    segments[0].move(move_direction[0] * move_distance, move_direction[1] * move_distance)

    # move todos os segmentos depois da cabeça da cobra
    for segmento in segments[1:]:
        temp_x = segmento.getCenter().getX()
        temp_y = segmento.getCenter().getY()
        segmento.move(pos_antiga_x - segmento.getCenter().getX(), pos_antiga_y - segmento.getCenter().getY())
        pos_antiga_x = temp_x
        pos_antiga_y = temp_y

        # detecta colisao de cada segmento com a cabeça apos movimenta-los
        if detect_collision(segments[0].getCenter(), segmento.getCenter()) or detect_out_of_bounds(segments[0].getCenter()):
            game_ended = True

    if detect_collision(segments[0].getCenter(), apple.getCenter()):
        grow(gf.Point(pos_antiga_x, pos_antiga_y), 'green')
        changeApplePos()

        

    time.sleep(0.15)



