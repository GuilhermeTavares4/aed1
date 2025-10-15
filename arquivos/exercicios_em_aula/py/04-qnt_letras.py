with open("exercicios_em_aula/txt/04-qnt_letras.txt", 'r') as arq:
    texto = arq.read()
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    qnt_letras = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    texto = texto.upper()
    for char in texto:
        if char in letras:
            qnt_letras[ord(char) - 65] += 1
    for i in range(len(qnt_letras)):
        print(f"{chr(65 + i)}: {qnt_letras[i]}")
