def num_divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


num = int(input("Digite um número maior que zero: "))
divisores = num_divisores(num)
print(divisores, ", ", len(divisores))