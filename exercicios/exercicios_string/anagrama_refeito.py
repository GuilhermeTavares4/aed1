def teste_anagrama(p1, p2):
    if len(p1) != len(p2):
        return False
    
    vetorp1, vetorqnt1 = preenche_vetores(p1)
    vetorp2, vetorqnt2 = preenche_vetores(p2)
    
    i = 0
    while i < len(vetorp1):
        if vetorp1[i] not in vetorp2 or vetorp2[i] not in vetorp1:
            return False
        i += 1

    i = 0
    while i < len(vetorp1):
        letra = vetorp1[i]
        num = vetorqnt1[i]
        if vetorp1.index(letra) == vetorp2.index(letra) and vetorqnt1.index(num) != vetorqnt2.index(num) and num != vetorqnt2[i]:
            return False
        i += 1
        
    return True

def preenche_vetores(palavra):
    vetorp = []
    vetorqnt = []
    for i in palavra:
        if i not in vetorp:
            vetorp.append(i)
            vetorqnt.append(1)
        else:
            vetorqnt[vetorp.index(i)] += 1
    return vetorp, vetorqnt


palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

if teste_anagrama(palavra1, palavra2):
    print("É um anagrama")
else:
    print("Não é um anagrama.")