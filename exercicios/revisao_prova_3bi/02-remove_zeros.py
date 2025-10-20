def cria_listas(lista):
    lista_positivos = []
    lista_negativos = []
    for num in lista:
        if num >= 0:
            lista_positivos.append(num)
        else:
            lista_negativos.append(num)
    print(lista)
    print(lista_positivos)
    print(lista_negativos)
    remove_zeros(lista_positivos, lista_negativos)


def remove_zeros(lista_positivos, lista_negativos):
    qnt_zeros = lista_positivos.count(0)

    lista_positivos = list(filter(lambda x: x != 0, lista_positivos))
    print(f"Havia {qnt_zeros} na lista dos positivos")
    print(f"Restaram {len(lista_positivos)} números na lista dos positivos e {len(lista_negativos)} na dos negativos")


lista = []
n = int(input("Digite quantos números você quer inserir na lista: "))
for i in range(n):
    lista.append(int(input("Digite um número a ser inserido na lista: ")))
cria_listas(lista)