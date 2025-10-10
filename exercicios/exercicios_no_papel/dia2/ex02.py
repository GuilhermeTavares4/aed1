def primos(a, b):
    if a < b:
        n1 = a
        n2 = b
    else:
        n1 = b
        n2 = a
    lista = []
    while n1 <= n2:
        i = n1 - 1
        while i > 1:
            if n1 % i == 0:
                break
            i -= 1
        if i == 1:
            lista.append(n1)
        n1 += 1
    return (lista)

a = int(input("inicio: "))
b = int(input("fim: "))
print(primos(a,b))