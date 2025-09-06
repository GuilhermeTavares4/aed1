soma = 0
n = 1
while n != 0:
    n = int(input("Digite um número: "))
    soma += n
if soma % 2 == 1:
    print(f"A soma dos valores ({soma}) é ímpar.")
    soma *= 2
print(soma)
 