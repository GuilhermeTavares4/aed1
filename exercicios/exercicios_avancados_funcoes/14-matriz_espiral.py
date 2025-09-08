'''
[01,02,03,04]
[12,13,14,05]
[11,16,15,06]
[10,09,08,07]

direita baixo esquerda cima repete
'''

def matriz_espiral(n):
    if n <= 1:
        print("babaca")
        return
    matriz = gera_matriz_vazia(n)
    posX = 0
    posY = 0
    direcao = [0, 1]
    valor = 1
    sentido_h = 1
    sentido_v = 1
    tem_zero = True

    while tem_zero:
        tem_zero = False
        matriz[posY][posX] = str(valor)
        posY += direcao[0] * sentido_h
        posX += direcao[1] * sentido_v

        if (matriz[posY][posX] != "0" or posX == n - 1 or posX == 0) and direcao[1] == 1:
            if matriz[posY][posX] != "0":
                posX -= direcao[1] * sentido_v
            sentido_v *= -1
            direcao[0] = 1
            direcao[1] = 0
        else:
            if (matriz[posY][posX] != "0" or posY == n - 1 or posY == 0) and direcao[0] == 1:
                if matriz[posY][posX] != "0":
                    posY -= direcao[0] * sentido_h
                sentido_h *= -1
                direcao[0] = 0
                direcao[1] = 1

        if matriz[posY][posX] == "0":
            valor += 1

        for lista in matriz:
            if "0" in lista:
                tem_zero = True

    for lista in matriz:
        i = 0
        while i < len(lista):
            if len(lista[i]) == 1:
                lista[i] = "0" + lista[i]
            i += 1
        
    for i in range(n):
        print(matriz[i])

    return


def gera_matriz_vazia(n):
    matriz = []
    for i in range(n):
        lista = []
        for j in range(n):
            lista.append("0")
        matriz.append(lista)

    return matriz


num = 9
matriz_espiral(num)
#gera_matriz_vazia(num)

