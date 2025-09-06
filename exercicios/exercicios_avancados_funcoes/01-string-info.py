def info_da_string(string):
    lista_info = []
    lista_string = string.split()
    num_palavras = len(lista_string)
    lista_info.append(num_palavras)
    num_chars = len(string)
    lista_info.append(num_chars)
    lista_info.append(media_len_palavras(string))
    lista_info.append(palavra_mais_longa(string))

    return lista_info

def media_len_palavras(string):
    lista_string = string.split()
    soma = 0
    i = 0
    while i < len(lista_string):
        soma += len(lista_string[i]) 
        i += 1
    media = soma / len(lista_string)

    return media

def palavra_mais_longa(string):
    palavra = ""
    maior_len = 0
    lista_string = string.split()
    for i in lista_string:
        if len(i) > maior_len:
            palavra = i
            maior_len = len(i)

    return palavra

string = "porra 123 aaa"
print(info_da_string(string))
