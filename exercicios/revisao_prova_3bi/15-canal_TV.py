import os.path

def read_valores(nome_arq, canal):
    if not os.path.exists(nome_arq):
        return False
    
    with open(nome_arq, 'r') as arq:
        dados = arq.read()
        dados = dados.splitlines()
        canal = str(canal)
        for i in range(len(dados)):
            dados[i] = dados[i].split(";")
            dados[i][1] = int(dados[i][1])
        dados =  soma_repetidos(dados)
        soma_audiencia = 0
        for value in dados.values():
            soma_audiencia += value
        porcentagem = dados[canal] / soma_audiencia * 100
        return f"{dados[canal]}, {soma_audiencia}, {porcentagem}%."


def soma_repetidos(dados):
    dados_sem_repetir = {}
    canais = []
    for item in dados:
        if item[0] not in canais:
            canais.append(item[0])
            dados_sem_repetir[item[0]] = item[1]
        else:
            dados_sem_repetir[item[0]] += item[1]
    return dados_sem_repetir


print(read_valores("15-canal_TV.txt", '4'))