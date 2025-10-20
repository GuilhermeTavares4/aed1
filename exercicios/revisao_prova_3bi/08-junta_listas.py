def junta_listas(lista1, lista2, lista3):
    lista_maior = [lista1] + [lista2] + [lista3]
    return lista_maior


def maior_valor(matriz):
    maior = matriz[0][0]
    for lista in matriz:
        for item in lista:
            if item > maior:
                maior = item
    return maior


listas = [[], [], []]
for i, lista in enumerate(listas):
    for j in range(5):
        num = int(input(f"Digite um número da lista {i + 1}: "))
        lista.append(num)

matriz = junta_listas(listas[0], listas[1], listas[2])
maior = maior_valor(matriz)
print(matriz)
print(f"O maior valor é: {maior}")