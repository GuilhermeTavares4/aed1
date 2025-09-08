def gera_anagramas(string):
    n = len(string)
    lista = []
    if n <= 1:
        return string
    
    for i in range(n):
        char = string[i]
        resto = string[:i] + string[i + 1:]
        print(gera_anagramas(resto))

        for j in gera_anagramas(resto):
            lista.append(char + j)

    return lista


def remove_ocorrencias_extras(lista):
    lista_limpa = []
    for item in lista:
        if item not in lista_limpa:
            lista_limpa.append(item)
            
    return lista_limpa


string = "erro"
anagrams = gera_anagramas(string)
print(remove_ocorrencias_extras(anagrams))