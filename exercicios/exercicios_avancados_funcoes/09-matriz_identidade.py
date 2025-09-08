def matriz_identidade(n):
    lista_final = []
    for i in range(n):
        lista_temp = []
        for j in range(n):
            if j == i:
                lista_temp.append(1)
            else:
                lista_temp.append(0)

        lista_final.append(lista_temp)

    return lista_final


num = 4
print(matriz_identidade(num))