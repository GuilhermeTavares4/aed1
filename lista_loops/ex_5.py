letra = input("Digite uma letra: ")
frase = input("Digite uma frase: ")
i = 0
qnt = 0
while i < len(frase):
    if letra == frase[i]:
        qnt += 1
    i += 1
print(f"A letra {letra} aparece {qnt} vezes na frase '{frase}'")