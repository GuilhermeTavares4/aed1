def add_produto(produto, qnt):
    if produto not in lista_produtos:
        lista_produtos.append(produto)
        qnt_produtos.append(qnt)
    else:
        qnt_produtos[lista_produtos.index(produto)] += qnt


def remove_produto(produto):
    if produto not in lista_produtos:
        print("O produto não ta na lista")
        return
    qnt_produtos.pop(lista_produtos.index(produto))
    lista_produtos.remove(produto)


def vende_produto(produto, qnt):
    if produto not in lista_produtos:
        print("O produto não ta na lista")
        return
    qnt_produtos[lista_produtos.index(produto)] -= qnt
    if qnt_produtos[lista_produtos.index(produto)] <= 0:
        qnt_produtos.pop(lista_produtos.index(produto))
        lista_produtos.remove(produto)


lista_produtos = []
qnt_produtos = []
comando = " "

while comando == "adicionar" or comando == "remover" or comando == "vender" or comando == " ":

    comando = input("Digite qual comando você quer realizar: 'adicionar', 'remover' ou 'vender'. Digite 'Fim' para sair: ")

    if comando == "adicionar":
        produto = input("Digite qual produto você quer adicionar: ")
        qnt = int(input("Digite quantos desse produto você quer adicionar: "))
        add_produto(produto, qnt)

    if comando == "remover":
        produto = input("Digite qual produto você quer remover: ")
        remove_produto(produto)
    
    if comando == "vender":
        produto = input("Digite qual produto você quer vender: ")
        qnt = int(input("Digite quantos desse produto você quer vender: "))
        vende_produto(produto, qnt)

    i = 0
    print("Lista")
    while i < len(lista_produtos):
        print(lista_produtos[i] + ": " + str(qnt_produtos[i]))
        i += 1
    