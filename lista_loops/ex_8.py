frase = input("Digite uma frase: ")
i = len(frase) - 1
inverso = ""
while i >= 0:
    inverso += frase[i]
    i -=1
print(inverso)
