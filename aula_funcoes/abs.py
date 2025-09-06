def absoluto(num):
    if num >= 0:
        return num
    return num * -1

numero = int(input("Digite um número: "))
valor_abs = absoluto(numero)
print(valor_abs)