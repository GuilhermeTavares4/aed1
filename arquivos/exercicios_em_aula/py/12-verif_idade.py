import os.path


def cria_pessoas(ano, arq1, arq2):
    if not os.path.exists(caminho + arq1):
        print('arquivo naoe xiste vai se foder')
        return

    with open(caminho + arq1, 'r') as arq:
        pessoas = []
        linhas = arq.readlines()
        for linha in linhas:
            info = linha.split(";")
            pessoa = {
                "nome": info[0],
                "data_nascimento": int(info[1])
            }
            pessoas.append(pessoa)
        
    write_pessoas(ano, arq2, pessoas)


def write_pessoas(ano, arq2, pessoas):
    with open(caminho + arq2, 'w') as arq:
        texto = ""
        for pessoa in pessoas:
            linha = pessoa["nome"] + ";"
            if ano - pessoa["data_nascimento"] - 1 > 18:
                linha += "maior de idade"
            elif ano - pessoa["data_nascimento"] - 1 == 18:
                linha += "entrando na maior idade"
            else:
                linha += "menor de idade"
            linha += "\n"
            texto += linha
        arq.write(texto)
            

caminho = 'txt/'

ano = int(input("Digite o ano atual: "))
arq1 = input("Digite o nome do primeiro arquivo: ")
arq2 = input("Digite o nome do segundo arquivo: ")

cria_pessoas(ano, arq1, arq2)

