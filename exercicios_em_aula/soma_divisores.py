n = int(input("Digite um número: "))
soma = 0
i = 1
while i <= int(n / 2):
    if n % i == 0:
        soma += i
        print(f"{n} é divisivel por {i}")
    i += 1
print(soma)