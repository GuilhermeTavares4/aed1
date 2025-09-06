def verifica_sudoku(matriz):
    
    #verifica por linha
    for linha in matriz:
        i = 1
        if not verifica_numeros(linha):
            return False

    #verifica por coluna
    i = 0
    while i < 9:
        col = gera_coluna(matriz, i)

        if not verifica_numeros(col):
            return False
        
        i += 1
    
    #verifica por quadrado
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            quadrado = gera_quadrado(matriz, i, j)

            if not verifica_numeros(quadrado):
                return False
            j += 3
            
        i += 3

    return True


def verifica_numeros(vetor):
    i = 1
    while i <= 9:
        if i not in vetor:
            return False
        i += 1
    return True

def gera_coluna(matriz, index):
    col = []
    for linha in matriz:
        col.append(linha[index])
    return col

def gera_quadrado(matriz, linha, coluna):
    quadrado = []
    i = linha
    while i < linha + 3:
        j = coluna
        while j < coluna + 3:
            quadrado.append(matriz[i][j])
            j += 1
        i += 1
    return quadrado




matriz = [[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7], [8,5,9,7,6,1,4,2,3], 
          [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6], [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,9]]

for linha in matriz:
    string = ""
    for num in linha:
        string += str(num) + " "
    print(string)

if verifica_sudoku(matriz):
    print("É válida.")
else:
    print("É inválida.")
