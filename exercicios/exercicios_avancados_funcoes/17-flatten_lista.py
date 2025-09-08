def flatten_list(coisa):
    lista_desaninhada = []

    for item in coisa:

        #verifica se nao é lista (de uma maneira bem porca)
        if "[" not in str(item):
            lista_desaninhada.append(item)

        else:
            lista_desaninhada += flatten_list(item)
            
    return lista_desaninhada
    

lista_aninhada = [1231513, [2, 3,[4, "fodase", 5]], [6, 7]]
print(flatten_list(lista_aninhada))

