def matriz_equilibrada(matriz):
    somas = []
    for linha in range(len(matriz)):
        temp_soma = 0
        for coluna in range(len(matriz[linha])):
            temp_soma +=  matriz[linha][coluna]
        somas.append(temp_soma)
        temp_soma = 0
        col = gera_coluna(matriz, linha)
        for i in col:
            temp_soma += i
        somas.append(temp_soma)
    print(somas)
    for i in somas:
        if somas[0] != i:
            return False
    return True




def gera_coluna(matriz, index):
    col = []
    for linha in matriz:
        col.append(linha[index])
    return col


matriz = [[2,7,6],
          [9,5,1],
          [4,3,8]]

print(matriz_equilibrada(matriz))