def add_lista(nome, lista):
    if nome in lista:
        return lista
    lista.append(nome)
    return lista


lista = ['guilherme', 'juan', 'murillo (RIP)']
nome = 'breno'

print(add_lista(nome, lista))