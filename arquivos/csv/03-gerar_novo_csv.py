def verif_algoritmo(nome):
    nome = nome.lower()
    if 'algoritmo' in nome or 'algoritmos' in nome:
        return True
    else:
        return False
    
with open ('disciplinas_filtrado_algoritmo_2025.csv', 'w', encoding='iso8859-1') as arq_novo:
    arq_novo.write("")

with open('disciplinasC3_2025.csv', 'r', encoding='iso8859-1') as arq, open ('disciplinas_filtrado_algoritmo_2025.csv', 'a', encoding='iso8859-1') as arq_novo:
    next(arq)
    linhas = arq.readlines()
    for linha in linhas:
        dados = linha.split(";")
        disciplina = dados[4]
        if verif_algoritmo(disciplina):
            arq_novo.write(linha)

        