def mult_matriz(matriz1, matriz2):

    if len(matriz1[0]) != len(matriz2):
        return "vai toman no cu nao da pra multiplicar essas matrizes"

    matriz_mult = []
    result = 0
    linha = 0
    
    while linha < len(matriz1):
        coluna = 0
        lista_temp = []

        while coluna < len(matriz2[0]):
            i = 0
            result = 0

            while i < len(matriz1[0]):
                result += matriz1[linha][i] * matriz2[i][coluna]
                i += 1

            lista_temp.append(result)
            coluna += 1

        matriz_mult.append(lista_temp)
        linha += 1

    return matriz_mult


matriz1 = [[1, 2], 
           [3, 4]]

matriz2 = [[2, 0], 
           [1, 2]]

print(mult_matriz(matriz1, matriz2 ))