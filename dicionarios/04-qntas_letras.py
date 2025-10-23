texto = 'aoijfaoijfoi'
qnt_letras = {}
for char in texto:
    if char not in qnt_letras:
        qnt_letras[char] = 1
    else:
        qnt_letras[char] += 1

print(qnt_letras)