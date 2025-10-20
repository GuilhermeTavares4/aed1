def verif_graduacao(nivel):
    nivel.replace('"', '')
    nivel = nivel.lower()
    if nivel == "graduação":
        return True
    else: 
        return False

with open('disciplinasC3_2025.csv', 'r', encoding='iso8859-1') as arq:
    next(arq)
    linhas = arq.readlines()
    niveis = []
    for linha in linhas:
        linha = linha.split(";")
        nivel = linha[1]
        niveis.append(nivel)
    niveis = filter(verif_graduacao, niveis)
    for a in niveis:
        print(a)
    

         