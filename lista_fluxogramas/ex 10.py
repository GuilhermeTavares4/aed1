c = int(input("Digite o comprimento da figura geométrica: "))
l = int(input("Digite o largura da figura geométrica: "))
if c <= 0 or l <= 0:
    print("Digite números positivos.")
else:
    if c == l:
        print("É um quadrado.")
    else:
        print("É um retângulo.")
