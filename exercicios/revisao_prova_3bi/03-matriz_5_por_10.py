def arruma_matriz(matriz):
    for i in range(len(matriz)):
        matriz[i] = matriz[i].replace(" ", "")
        matriz[i] = matriz[i].split(",")
        if len(matriz[i]) != 10:
            return "matriz ta errada vsf"
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz


def exibe_por_coluna(matriz):
    if type(matriz) is not list:
        return "corno"
    
    colunas = []
    for i in range(len(matriz[0])):
        coluna = []
        for j in range(len(matriz)):
            coluna.append(matriz[j][i])
        colunas.append(coluna)
    for item in colunas:
        print(item)


linhas = 5
matriz = []
for i in range(linhas):
    linha = input("Digite os 10 elementos da linha separados por vírgula: ")
    matriz.append(linha)



# matriz = [
#     "1,2,3,4,5,6,7,8,  9, 0",
#     "5,3,1,7,7,5,3,2,1,0",
#     "5,3,1,7,7,5,3,2,1,0",
#     "5,3,1,7,7,5,3,2,1 ,0",
#     "5,3,1,7,7,5,3,2,1,0"
# ]
print(exibe_por_coluna(arruma_matriz(matriz)))
