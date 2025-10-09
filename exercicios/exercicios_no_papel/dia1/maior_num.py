def maior_num(num, qnt):
    lista_num = list(str(num))
    if num < 0:
        lista_num = lista_num[1:]
    if qnt > len(lista_num):
        return "agradeça a esse return aqui que você está lendo agora, pois seu editor de texto e possívelmente seu computador iriam travar." 
    lista_sort = sorted(lista_num)
    if num > 0:
        lista_sort = lista_sort[::-1]
    i = 0
    j = 0
    casas = qnt
    min_i = 0
    num_final = ""
    while casas != 0:
        if casas <= len(lista_num) - i:
            if lista_num[i] == lista_sort[j]:
                num_final += lista_num[i]
                min_i = i + 1
                lista_sort.pop(j)
                j = 0
                casas -= 1
            else:
                i += 1
        else:
            i = min_i
            j += 1
    if num < 0:
        num_final = "-" + num_final
    return num_final

print(maior_num(-5452, 1))
print(maior_num(5452, 2))
print(maior_num(53892, 2))
print(maior_num(-347, 2))
print(maior_num(-53892, 2))
print(maior_num(-53892, 3))
print(maior_num(12121212, 4))
print(maior_num(-12121212, 4))



