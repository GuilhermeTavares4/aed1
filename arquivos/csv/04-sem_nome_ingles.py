def tem_ingles(dados):
    if dados[6] == '\n':
        return False
    else:
        return True

with open ('disciplinas_filtrado_ingles_2025.csv', 'w', encoding='iso8859-1') as arq_novo:
    arq_novo.write("")

with open('disciplinasC3_2025.csv', 'r', encoding='iso8859-1') as arq, open ('disciplinas_filtrado_ingles_2025.csv', 'a', encoding='iso8859-1') as arq_novo:
    next(arq)
    linhas = arq.readlines()
    for linha in linhas:
        dados = linha.split(";")
        print(dados[6])
        if not tem_ingles(dados):
            arq_novo.write(linha)

        