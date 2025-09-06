n = int(input("Digite um número: "))
i = 0
termo1 = 0
termo2 = 1
while i < n:
    print(termo1)
    termo1 = termo1 + termo2
    termo2 = termo1 - termo2
    i += 1
      