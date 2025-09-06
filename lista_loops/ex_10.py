frase = input("Digite uma frase: ")
i = 0
frase2 = ""
while i < len(frase):
    if frase[i] != " ":
        frase2 += frase[i]
    i += 1
print(frase2)