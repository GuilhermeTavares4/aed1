def organiza_palavras(string):
    lista_palavras = string.split()
    lista_palavras = organiza_tamanho(lista_palavras)
    lista_palavras = organiza_alfabeticamente(lista_palavras)
    return lista_palavras


def organiza_tamanho(lista):
    
    i = 0
    while i < len(lista):
        j = 0
        while j < len(lista) - i - 1: 
            if len(lista[j]) > len(lista[j + 1]):
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
            j += 1
        i += 1
        
    return lista


def organiza_alfabeticamente(lista):

    i = 0
    while i < len(lista):
        j = 0
        while j < len(lista) - i - 1: 
            if len(lista[j]) == len(lista[j + 1]):
                k = 0
                while k < len(lista[j]) and lista[j][k] == lista[j + 1][k]:
                     k += 1
                if ord(lista[j][k]) > ord(lista[j + 1][k]): 
                    temp = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temp
            j += 1
        i += 1

    return lista


string = "banana uva abacaxi pera morango"
print(organiza_palavras(string))