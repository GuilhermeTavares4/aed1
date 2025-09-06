palavra = input("Digite uma palavra: ")
i = 0
while palavra != "":
    palavra = palavra[1:]
    i += 1
print(f"A palavra tem {i} caracteres.")