palavra = input("Digite uma palavra: ")
i = 0
palavraNova = ""
digitoNovo = ""
consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = "aeiou"
while i < len(palavra):
    j = 0
    while j < len(consoantes):
        if palavra[i] == consoantes[j]:
            if palavra[i] == "z":
                palavraNova += "b"
            else:
                palavraNova += consoantes[j + 1]
        j += 1
    j = 0
    while j < len(vogais):
        if palavra[i] == vogais[j]:
            palavraNova += str(j + 1)
        j += 1
    i += 1
print(palavraNova)