import os.path
    
def verif_linha(linha):
    if "#" in linha or '&' in linha or "*" in linha:
        return False
    else:
        return True


def read_linhas(arq_linhas):
    if not os.path.exists(caminho + arq_linhas):
        return 1
    
    with open(caminho + arq_linhas, 'r') as arq:
        linhas = arq.readlines()

    write_linhas(linhas)
    return 0
    
def write_linhas(linhas):
    linhas_sem_os_bgl = filter(verif_linha, linhas)
    texto = ""
    for linha in linhas_sem_os_bgl:
        texto += linha
    with open(caminho + "16-linhas_filtradas.txt", 'w') as arq:
        arq.write(texto)

caminho = 'txt/'

print(read_linhas('16-linhas_nao_filtradas.txt'))