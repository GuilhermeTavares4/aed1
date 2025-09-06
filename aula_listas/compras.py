listaCompras = []
item = input("Adicione um item à lista: ")
while item != "":
    listaCompras.append(item)
    item = input("Adicione um item à lista: ")
i = 0
while i < len(listaCompras):
    print(f"Item {i + 1}: {listaCompras[i]}")
    i += 1


