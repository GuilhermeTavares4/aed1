def verif_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
def quantos_dias(dia, mes, ano):
    i = 1
    dias = 0
    while i < mes:
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10:
            dias += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            dias += 30
        elif i == 2 and not verif_ano_bissexto(ano):
            dias += 28
        else:
            dias += 29
        i += 1
    dias += dia - 1
    return dias

print(quantos_dias(28,7,2004))
            