def corta_lista(lista, num):
    lista_final = []
    lista_temp = []
    for i in range(len(lista)):
        lista_temp.append(lista[i])
        if len(lista_temp) == num:
            lista_final.append(lista_temp)
            lista_temp = []
    if lista_temp != []:
        lista_final.append(lista_temp)

    return lista_final



num = 5


lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

print(corta_lista(lista, num))



