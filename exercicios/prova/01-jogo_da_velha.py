def verifica_jogo(matriz):
    for linha in matriz:
        if linha.count("X") == 3:
            return "X"
        if linha.count("O") == 3:
            return "O"
    for i in range(len(matriz[0])):
        col = gera_coluna(matriz, i)
        if col.count("X") == 3:
            return "X"
        if col.count("O") == 3:
            return "O"
    diag1 = []
    diag2 = []
    i = 0
    j = len(matriz) - 1
    while i < len(matriz):
        diag1.append(matriz[i][i])
        diag2.append(matriz[i][j])
        i += 1
        j -= 1

    if diag1.count("X") == 3 or diag2.count("X") == 3:
        return "X"
    if diag1.count("O") == 3 or diag2.count("O") == 3:
        return "O"
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] != "X" and matriz[linha][coluna] != "O":
                return "Jogo inacabado"
    return "Deu velha." 
 

def gera_coluna(matriz, index):
    col = []
    for linha in matriz:
        col.append(linha[index])
    return col

jogo = [["O", "X", "O"],
        ["O", "", "X"],
        ["O", "X", "O"]]

print(verifica_jogo(jogo))