def notInList(word, lista):
    for item in lista:
        if item[0] == word:
            return False
    return True

def organiza_ordem(lista):
    i = 0
    while i < len(lista):
        j = 1
        while j < len(lista) - i:
            if lista[j - 1][1] < lista[j][1]:
                temp = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = temp
            j += 1
        i += 1
    return lista

def ordena(texto):
    texto = texto.lower()
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto1 = ""
    for char in texto:
        if char in alfabeto:
            texto1 += char
        else:
            texto1 += " "
    texto1 = texto1.split()
    lista = []
    for palavra in texto1:
        if notInList(palavra, lista):
            lista.append([palavra, texto1.count(palavra)])
    return organiza_ordem(lista)

texto = "a,a,a,a,b,b,c,c,c,d"
print(ordena(texto))