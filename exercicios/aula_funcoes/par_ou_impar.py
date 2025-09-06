def ParOuImpar(num):
    if num % 2 == 0:
        return "par"
    return "ímpar"

numero = int(input("Digite um número: "))

print(f"O número é {ParOuImpar(numero)}.")