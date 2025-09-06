def separa_letras(string):
    lista = []
    i = 1
    qnt = 1
    while i < len(string):
        if string[i] == string[i - 1]:
            qnt += 1
        else:
            lista.append(string[i - 1] * qnt)
            qnt = 1
        i += 1
    lista.append(string[i - 1] * qnt)
    
    return lista
    


def compacta_string(string):
    nova_string = ""
    lista_string = separa_letras(string)
    for i in lista_string:
        nova_string += i[0] + str(i.count(i[0]))
    return nova_string

palavra = input("Digite uma palavra: ")

print(compacta_string(palavra))