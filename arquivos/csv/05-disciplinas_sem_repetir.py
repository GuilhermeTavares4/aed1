with open('disciplinasC3_2025.csv', 'r') as arq:
    next(arq)
    linhas = arq.read()
    linhas = linhas.splitlines()
    disciplinas = []
    for linha in linhas:
        dados = linha.split(";")
        if dados[4].lower() not in map(lambda d: d.lower(), disciplinas):
            disciplinas.append(dados[4])
with open('disciplinas_sem_repetir_2025.csv', 'w', encoding='UTF-8') as arq:
    texto = ""
    for disciplina in disciplinas:
        texto += disciplina + "\n"
    arq.write(texto)