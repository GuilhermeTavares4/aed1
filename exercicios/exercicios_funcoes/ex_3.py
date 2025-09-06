def gera_vetor(string):
    stringUpper = string.upper()
    vetor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in stringUpper:
        vetor[ord(i) - 65] += 1
    return vetor


def verif_anagrama(vetor1, vetor2):
    vetor_novo = []
    i = 0
    while i < len(vetor1):
        vetor_novo.append(vetor1[i] - vetor2[i])   
        i += 1  
    for num in vetor_novo:
        if num != 0:
            return False
    return True

def agrupa_lista(lista):
    lista_final = []
    lista_remove = lista
    for elemento1 in lista:
        lista_anagrama = []
        ocorrencias = lista.count(elemento1)
        i = 0
        while i < ocorrencias:
            lista_anagrama.append(elemento1)
            lista_remove.remove(elemento1)
            i += 1
        for elemento2 in lista:
            if elemento2 in lista_remove:
                vetor1 = gera_vetor(elemento1)
                vetor2 = gera_vetor(elemento2)
                if verif_anagrama(vetor1, vetor2):
                    lista_anagrama.append(elemento2)
        lista_final.append(lista_anagrama)
    return lista_final


lista_palavras = ["roma", "roma", "amor", "fodase", "farsa", "safra", "rafas"]


print(agrupa_lista(lista_palavras))

'''vetor1 = gera_vetor("romar")
vetor2 = gera_vetor("amor")

if verif_anagrama(vetor1, vetor2):
    print("É anagrama")
else:
    print("Não é anagrama")
'''
