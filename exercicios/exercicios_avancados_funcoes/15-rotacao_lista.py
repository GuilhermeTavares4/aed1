def rotaciona_lista(lista, n):
    lista_comp = lista
    for num in range(n):
        lista_temp = []
        j = len(lista_comp) - 1
        for i in range(0, len(lista_comp)):
            lista_temp.append(lista_comp[j % len(lista_comp)])
            j += 1
        lista_comp = lista_temp
    return lista_comp


lista = [1, 2, 3, 4, 5]
num = 2
print(rotaciona_lista(lista, num))