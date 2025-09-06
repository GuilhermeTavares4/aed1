char = input("Digite um caractere: ")
n = int(input("Digite um número: "))
i = 0
quadrado = ""
while i < n:
    j = 0
    while j < n:
        quadrado += char
        j += 1
    quadrado += "\n"
    i += 1
print(quadrado)