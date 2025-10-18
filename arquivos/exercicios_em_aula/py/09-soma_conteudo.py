def nao_eh_comentario(linha):
    if len(linha) >= 2:
        if linha[0:2] == "//":
            return False
    return True


def soma_conteudo(arq1, arq2):
    caminho = "txt/"
    try:
        arq = open(caminho + arq1, "r")
    except:
        print("o arquivo de origem não existe")
        return
    else:
        linhas = arq.readlines()
        linhas_sem_comentario = list(filter(nao_eh_comentario, linhas))
        texto = "".join(linhas_sem_comentario)
        arq.close()
    
    try:
        with open(caminho + arq2, 'r+') as arq:
            arq.seek(0, 2)
            arq.write(texto)
    except:
        print("arquivo de destino não existe")


arq1 = input("Digite o nome do primeiro arquivo: ")
arq2 = input("Digite o nome do segundo arquivo: ")
soma_conteudo(arq1, arq2)