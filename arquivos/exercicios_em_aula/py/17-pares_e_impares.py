with open('txt/17-pares.txt', 'r') as arq_pares, open('txt/17-impares.txt', 'r') as arq_impares:
    pares = arq_pares.readlines()
    impares = arq_impares.readlines()
    pares_e_impares = pares + impares
    for i in range(len(pares_e_impares)):
        if "\n" in pares_e_impares[i]:
            pares_e_impares[i] = pares_e_impares[i][:-1]
        pares_e_impares[i] = int(pares_e_impares[i])
    pares_e_impares.sort()

with open('txt/17-pares_e_impares.txt', 'w') as arq:
    txt = ""
    for num in pares_e_impares:
        txt += str(num) + '\n'
    arq.write(txt)