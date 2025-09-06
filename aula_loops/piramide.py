char = input("Digite um tijolo")
altura = int(input("Digite a altura"))
i = 0
piramide = ""
while i < altura:
    j = 0
    while j < altura - i:
        piramide += " "
        j += 1
    j = 0
    while j < 1 + i * 2:
        piramide += char
        j += 1
    piramide += "\n"
    i += 1
print(piramide)
