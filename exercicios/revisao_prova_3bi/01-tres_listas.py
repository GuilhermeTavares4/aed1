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


n = int(input("Digite quantos números você quer inserir na lista: "))
lista = []
for i in range(n):
    lista.append(int(input("Digite um número a ser inserido na lista: ")))

cria_listas(lista)