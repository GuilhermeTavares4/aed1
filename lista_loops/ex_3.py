vogais = "aeiou"
palavra = input("Digite uma palavra: ")
i = 0
qntVogais = 0
while i < len(palavra):
    vogal = False
    j = 0
    while j < len(vogais) and vogal == False:
        if palavra[i] == vogais[j]:
            qntVogais +=1
            vogal = True
        j += 1
    i +=1
print(f"A palavra tem {qntVogais} vogais.")
