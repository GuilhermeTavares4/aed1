def produto_cartesiano(lista1, lista2):
    lista_final = []
    for i in lista1:
        for j in lista2:
            lista_final.append([i, j])    
    return lista_final


lista1 = [1,2,3]
lista2 = ['a','b']
print(produto_cartesiano(lista1, lista2))