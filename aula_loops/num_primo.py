import math
limite = int(input("Digite um número: "))
i = 2
while i <= limite:
    primo = True
    j = int(math.sqrt(i))
    while j > 1 and primo == True:
        if i % j == 0:
            primo = False
        j -= 1
    if primo:
        print(f"{i} é número primo.")
    i +=1
        