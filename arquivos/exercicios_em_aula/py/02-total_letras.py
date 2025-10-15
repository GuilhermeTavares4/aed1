with open("exercicios_em_aula/txt/02-total_letras.txt", "r") as arq:
    texto = arq.read()
    texto = texto.lower()
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    count_vogais = 0
    count_consoantes = 0
    count_outros = 0
    for char in texto:
        if char in vogais:
            count_vogais += 1
        elif char in consoantes:
            count_consoantes += 1
        else:
            count_outros += 1
            print(char)
    print(f"O arquivo tem {count_vogais} vogais, {count_consoantes} consoantes e {count_outros} caracteres especiais")