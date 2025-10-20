def soma_matriz(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "nao da pra somar essas porra de matriz ai"
    matriz_soma = []
    for i in range(len(matriz1)):
        linha_soma = []
        for j in range(len(matriz1[i])):
            linha_soma.append(matriz1[i][j] + matriz2[i][j])
        matriz_soma.append(linha_soma)
    return matriz_soma


matriz1 = [[1, 2],
           [3, 4]]

matriz2 = [[5,6],
           [7,8]]

print(soma_matriz(matriz1, matriz2))