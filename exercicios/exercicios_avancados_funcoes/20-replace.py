def replace(string, original, novo, qnt = 0):
    cont = 0
    lista = string_to_list(string)
    for i in range(len(lista)):
        if qnt == 0 or cont < qnt:
            if lista[i] == original:
                lista[i] = novo   
                cont += 1     
    string_nova = list_to_string(lista)

    return string_nova


def string_to_list(string):
    lista = []
    string_temp = ""
    for i in range(len(string)):
        if string[i] != " ":
            string_temp += string[i]
        else:
            if i != len(string) - 1:
                lista.append(string_temp)
                string_temp = ""

    lista.append(string_temp)

    return lista


def list_to_string(lista):
    string = ""
    for i in lista:
        string += i
        string += " "
    string = string[:-1]

    return string


string = "estou repetindo essa frase varias vezes . estou repetindo essa frase varias vezes . estou repetindo essa frase varias vezes ."
print(replace(string, "varias", "algumas", 2))