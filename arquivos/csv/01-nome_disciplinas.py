with open('disciplinasC3_2025.csv', 'r', encoding='iso8859-1') as arq:
    next(arq)
    linhas = arq.readlines()
    disciplinas = []
    for linha in linhas:
        linha = linha.split(";")
        disciplina = linha[4]
        disciplinas.append(disciplina)
    for a in disciplinas:
        print(a)
    

         