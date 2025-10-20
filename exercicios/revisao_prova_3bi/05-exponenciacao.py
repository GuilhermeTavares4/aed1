def exponenciacao(base, expoente):
    if expoente == 1:
        return base
    if expoente == 0:
        return 1
    return base * exponenciacao(base, expoente - 1)


print(exponenciacao(3, 4))