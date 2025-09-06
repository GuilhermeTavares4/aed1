n = 1
while n <= 1000:
    strN = str(n)
    inverso = ""
    indiceFim = len(strN) - 1
    while indiceFim >= 0:
        inverso += strN[indiceFim]
        indiceFim -= 1
    if strN == inverso:
        print(inverso)
    n += 1