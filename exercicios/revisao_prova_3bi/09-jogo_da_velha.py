def verifica_jogo(matriz):
    for linha in matriz:
        if linha.count("X") == 3:
            return "X venceu"
        if linha.count("O") == 3:
            return "O venceu"
    for i in range(len(matriz[0])):
        col = gera_coluna(matriz, i)
        if col.count("X") == 3:
            return "X venceu"
        if col.count("O") == 3:
            return "O venceu"
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
        return "X venceu"
    if diag1.count("O") == 3 or diag2.count("O") == 3:
        return "O venceu"
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] != "X" and matriz[linha][coluna] != "O":
                return "inacabado"
    return "Deu velha." 
 

def gera_coluna(matriz, index):
    col = []
    for linha in matriz:
        col.append(linha[index])
    return col


def verifica_jogada(char, linha, coluna):
    if char != "X" and char != "O":
        return False
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False
    if tabuleiro[linha][coluna] != "":
        return False
    return True


def executa_jogada(jogador_atual, linha, coluna):
    if jogador_atual == "jogador1":
        tabuleiro[linha][coluna] = "X"  
    else:
        tabuleiro[linha][coluna] = "O"


def printa_tabuleiro():
    for linha in tabuleiro:
        print(linha)


def loop_do_jogo():
    situacao = "inacabado"
    jogador_atual = "jogador1"
    while situacao == "inacabado":
        while True:
            if jogador_atual == "jogador1":
                jogada = input("Jogador 1, digite onde você quer colocar a porra do 'X': ") # input: 1,2 (exemplo)
                char = "X"
            else:
                jogada = input("Jogador 2, digite onde você quer colocar a porra do 'O': ")
                char = "O"

            jogada = jogada.replace(" ", "")
            jogada = jogada.split(",")
            linha = int(jogada[0])
            coluna = int(jogada[1])
            if verifica_jogada(char, linha, coluna) != False:
                break
            else:
                print("jogada inválida ou vc é burro ou o codigo ta errado (vc é burro)")

        executa_jogada(jogador_atual, linha, coluna)
        printa_tabuleiro()
        if jogador_atual == "jogador1":
            jogador_atual = "jogador2"
        else:
            jogador_atual = "jogador1"
        situacao = verifica_jogo(tabuleiro)
    print(situacao)
        

tabuleiro = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

loop_do_jogo()