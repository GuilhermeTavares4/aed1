numero = int(input("digite um número: "))
i = 0
while i <= numero:
    j = 0
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1 