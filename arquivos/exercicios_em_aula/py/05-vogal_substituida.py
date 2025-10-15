texto = ""

with open("exercicios_em_aula/txt/05-vogal_substituida_original.txt", "r") as arq:
    texto = arq.read()

with open("exercicios_em_aula/txt/05-vogal_substituida_novo.txt", "w") as arq:
    texto_novo = ""
    vogais = 'aeiou'
    for char in texto:
        if char not in vogais:
            texto_novo += char
        else:
            texto_novo += "*"
    arq.write(texto_novo)

