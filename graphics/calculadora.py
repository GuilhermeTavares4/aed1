import graphics as gf
import math

def generateBackground():
    background = gf.Rectangle(gf.Point(window_size / 4, window_size / 8), gf.Point(window_size * 3 / 4, window_size * 7 / 8))
    background.draw(win)

def generateButtons():
    button_posX = 220
    button_posY = 200
    for i, text in enumerate(buttons.keys()):
        spawnPoint = gf.Point(button_posX, button_posY)
        buttons[text] = spawnPoint
        button = gf.Circle(spawnPoint, button_radius)
        button.draw(win)
        text = gf.Text(spawnPoint, text)
        text.draw(win)
        button_posX += 50
        if (i + 1) % 4 == 0:
            button_posY += button_radius * 2 + 10
            button_posX = 220

def generateScreen():
    screen = gf.Rectangle(gf.Point(200, 100), gf.Point(400, 150))
    screen.draw(win)


def getButtonClicked(click):
    for key, button_pos in buttons.items():
        distance = math.sqrt((click.getX() - button_pos.getX()) ** 2 + (click.getY() - button_pos.getY()) ** 2)
        if distance <= button_radius:
            return key
    return ''

def isActionValid(action):
    global used_expression
    if action == '':
        return False
    if len(used_expression) != 0:
        if used_expression[-1] in operations and action in operations:
            return False
        if used_expression[-1] == ',' and action not in numbers:
            return False
        if used_expression[-1] not in numbers and action == ',':
            return False
        if used_expression not in numbers and action == '=':
            return False
    return True
        

def updateShownExpression(char):
    global shown_expression
    shown_expression += char
    if len(used_expression) > 1:
        if used_expression[-1] not in numbers or char not in numbers:
            shown_expression += ' ' # arrumar esse coco aqui

    expression_text.setText(shown_expression)

window_size = 600

buttons =  {
    'AC': '',
    'sqrt': '',
    '^': '',
    '/': '',
    '7': '',
    '8': '',
    '9': '',
    'X': '',
    '4': '',
    '5': '',
    '6': '',
    '-': '',
    '1': '',
    '2': '',
    '3': '',
    '+': '',
    '0': '',
    ',': '',
    'del': '',
    '=': ''
 }

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
operations = ['+', 'sqrt', '-', 'X', '/', '^']
shown_expression = ""
used_expression = ""

button_radius = 20
win = gf.GraphWin('Janelha', window_size, window_size)
generateBackground()
generateButtons()
generateScreen()
expression_text = gf.Text(gf.Point(300, 125), shown_expression)
expression_text.draw(win)
previous_char = ""

while True:
    click = win.getMouse()
    action = getButtonClicked(click)
    if isActionValid(action):
        updateShownExpression(action)
        if action == 'AC':
            used_expression = ''
            shown_expression = ''
            continue
        
        used_expression += action
        if action == 'del':
            break
        


