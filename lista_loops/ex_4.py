i = 1
limite = 1000
qnt = 0
divisor = 7
while i <= limite:
    if i % divisor == 0:
        qnt += 1
    i += 1
print(f"{qnt} números de 1 até {limite} são divisíveis por {divisor}")