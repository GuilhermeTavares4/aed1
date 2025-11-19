import graphics as gf
import math

def generateBackground():
    background = gf.Rectangle(gf.Point(window_size / 4, window_size / 8), gf.Point(window_size * 3 / 4, window_size * 7 / 8))
    background.draw(win)

def generateButtons():
    button_x_pos = 220
    button_y_pos = 200
    for i, text in enumerate(buttons.keys()):
        spawnPoint = gf.Point(button_x_pos, button_y_pos)
        buttons[text] = spawnPoint
        button = gf.Circle(spawnPoint, button_radius)
        button.draw(win)
        text = gf.Text(spawnPoint, text)
        text.draw(win)
        button_x_pos += 50
        if (i + 1) % 4 == 0:
            button_y_pos += button_radius * 2 + 10
            button_x_pos = 220

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
        if str(used_expression[-1])[0] in numbers and action == 'sqrt':
            return False
        if str(used_expression[-1]) in operations and action in operations and action != 'sqrt':
            return False
        if used_expression[-1] == ',' and action not in numbers:
            return False
        if str(used_expression[-1])[0] not in numbers and action == ',':
            return False
        if str(used_expression[-1])[0] not in numbers and action == '=':
            return False
    return True
        

def updateShownExpression(char):
    char = str(char)
    global shown_expression
    if len(used_expression) > 0:
        if (str(used_expression[-1])[0] not in numbers or char not in numbers) and char != ',' and used_expression[-1] != ',':
            shown_expression += ' '
    shown_expression += char
    expression_text.setText(shown_expression)


def transform_str_into_num(expression):
    for i, item in enumerate(expression):
        if str(item)[0] in numbers and str(item)[0] in numbers:
            expression[i] = float(item)

    return expression


def do_the_math(expression):
    if len(expression) == 1:
        return expression
    if 'sqrt' in expression:
        op_index = expression.index('sqrt')
        temp_result = math.sqrt(expression[op_index + 1]) 

    elif '^' in expression:
        op_index = expression.index('^')
        temp_result = expression[op_index - 1] ** expression[op_index + 1]
        
    elif 'x' in expression:
        op_index = expression.index('x')
        temp_result = expression[op_index - 1] * expression[op_index + 1]

    elif '/' in expression:
        op_index = expression.index('/')
        temp_result = expression[op_index - 1] / expression[op_index + 1]

    elif '+' in expression:
        op_index = expression.index('+')
        temp_result = expression[op_index - 1] + expression[op_index + 1]

    elif '-' in expression:
        op_index = expression.index('-')
        temp_result = expression[op_index - 1] - expression[op_index + 1]
    
    expression[op_index + 1] = temp_result
    if expression[op_index] != 'sqrt':
        expression.pop(op_index - 1)
        expression.pop(op_index - 1)
    else:
        expression.pop(op_index)

    return do_the_math(expression)




window_size = 600

buttons =  {
    'AC': '',
    'sqrt': '',
    '^': '',
    '/': '',
    '7': '',
    '8': '',
    '9': '',
    'x': '',
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
operations = ['+', 'sqrt', '-', 'x', '/', '^']
shown_expression = ""
used_expression = []

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
        if action == '=' and len(used_expression) >= 2:
            used_expression = do_the_math(transform_str_into_num(used_expression))
            shown_expression = ''
            updateShownExpression(str(used_expression[0]))

            continue
        if  action == 'AC':
            used_expression = []
            shown_expression = ''
            updateShownExpression('')
            continue
        updateShownExpression(action)
        if len(used_expression) > 0:
            if str(used_expression[-1])[0] in numbers and action[0] in numbers or action == ',':
                used_expression[-1] += action
            else:
                used_expression.append(action)

        else:
            if action != 'sqrt':
                used_expression.append(action)
            else:
                used_expression.insert(-1, action)

        print(used_expression)


#coisas a fazer:
#    arrumar a ordem das operaçoes
#    botar sqrt antes do valor adicionado