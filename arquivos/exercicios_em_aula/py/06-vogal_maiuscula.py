def vogal_maiuscula(arq1, arq2):
    texto = ""
    arq1 = "exercicios_em_aula/txt/" + arq1
    arq2 = "exercicios_em_aula/txt/" + arq2
    with open(arq1, "r") as arq:
        texto = arq.read()

    with open(arq2, "w") as arq:
        texto_novo = ""
        vogais = "aeiou"
        for char in texto:
            if char in vogais:
                texto_novo += char.upper()
            else:
                texto_novo += char
        arq.write(texto_novo)


arq1 = input("Digite o nome do primeiro arquivo (sem o caminho): ")
arq2 = input("Digite o nome do segundo arquivo para sobrescrever (sem o caminho): ")

vogal_maiuscula(arq1, arq2)
