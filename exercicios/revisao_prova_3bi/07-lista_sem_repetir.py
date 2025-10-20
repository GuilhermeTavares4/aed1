def ordena_listas(lista1, lista2):
    lista_nova = lista1 + lista2
    lista_sem_repetir = []
    for item in lista_nova:
        if item not in lista_sem_repetir:
            lista_sem_repetir.append(item)

    return bubble_sort(lista_sem_repetir)


def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista


lista = ordena_listas([5, 3, 4], [2, 3,1])
soma = 0
for i in lista:
    soma += i
print(lista, soma)