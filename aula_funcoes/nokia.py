def texto_pra_num(texto):
    lista = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    senhaNova = ""
    for contTexto in range(len(texto)):
        char = texto[contTexto]
        contLista = 0
        while contLista < len(lista):
            if char in lista[contLista]:
                contador = lista[contLista].index(char)
                senhaNova += str(contLista) * (contador + 1)
            contLista += 1
        senhaNova += "_"
    return senhaNova

    
def num_pra_texto(num):
    lista = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    textoNovo = ""
    contNum = 0
    while contNum < len(num):
        charNum = num[contNum]
        qntRepete = repeteNum(num, contNum)
        contNum += qntRepete + 1
        charLetra = lista[int(charNum)][qntRepete]
        textoNovo += charLetra
        contNum += 1
    return textoNovo

def repeteNum(num, i):
    j = 0
    while num[i] != "_":
        j += 1
        i += 1
    j -= 1
    return j

texto = 'oi sumido'

num = "666_444_0_7777_88_6_444_3_666_"

print(texto_pra_num(texto))
print(num_pra_texto(num))
