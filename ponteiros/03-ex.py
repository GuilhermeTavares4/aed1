def incrementa(x):
    print(x, id(x))
    x[0] += 1
    print(x, id(x))

    x[0] += 1
    print(x, id(x))

x = [15]
print(x, id(x))
incrementa(x)
print(x, id(x))
