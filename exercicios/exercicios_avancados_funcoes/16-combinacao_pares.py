def combinacao_pares(lista):
    lista_pares = []
    for i in lista:
        for j in lista[i:]:
            lista_pares.append([i, j])
    return lista_pares


lista = [1,2,3,4,5]
print(combinacao_pares(lista))