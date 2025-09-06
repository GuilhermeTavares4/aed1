import math
def primo(n):
    i = int(math.sqrt(n))
    if n == 0 or n == 1:
        return False
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

n = int(input("Digite um número: "))

if primo(n):
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")