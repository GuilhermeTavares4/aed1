def pot(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        negativo = True
        exp = exp * -1
    else:
        negativo = False
    result = 1
    
    while exp > 0:
        result *= base
        exp -= 1
    if negativo:
        result = 1 / result
    return result 


#recursiva
'''
def pot(base, exp):
    if exp > 0:
        return base * pot(base, exp - 1)
    return True
'''

print(pot(3, 3))