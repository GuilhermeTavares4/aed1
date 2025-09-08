def  transposicao(matriz):
    i = 1
    while i < len(matriz):
        if len(matriz[i - 1]) != len(matriz[i]):
            return "filho da puta faz o bagulho direito"  
        i += 1    

    matriz_transposta = []
    i = 0
    while i < len(matriz[0]):
        lista_temp = []
        for j in range(len(matriz)):
            lista_temp.append(matriz[j][i])
        matriz_transposta.append(lista_temp)
        i += 1

    return matriz_transposta


matriz = [[1, 2, 3, 4,], [5, 6, 7, 8], [9, 10, 11, 12]]
print(transposicao(matriz))