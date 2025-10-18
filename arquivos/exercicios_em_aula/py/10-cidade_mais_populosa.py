import os.path

def cidade_mais_populosa(arq1, arq2):
    if not os.path.exists("txt/" + arq1):
        print("O arquivo não existe.")
        return
    
    caminho = 'txt/'
    cidades_info = {}
    with open(caminho + arq1, 'r', encoding='UTF-8') as arq1:
        linhas = arq1.readlines()
        for linha in linhas:
            i = 0
            while linha[i] != " " or linha[i + 1] != " ":
                i += 1
            cidade = linha[0:i]
            i += 1
            while linha[i] == " " and linha[i + 1] == " ":
                i += 1
            habitantes = linha[i + 1:]
            cidades_info[cidade] = int(habitantes)

    cidade_max = (max(cidades_info.items(), key=lambda k: k[1]))

    with open(caminho + arq2, 'w' , encoding='UTF-8') as arq2:
        arq2.write(f'{cidade_max[0]}: {cidade_max[1]}')


cidade_mais_populosa("10-cidade_mais_populosa_read.txt", "10-cidade_mais_populosa_write.txt")