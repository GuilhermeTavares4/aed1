def descompacta(sigla):
    nova_sigla = ""
    vetor_sigla = separa_num_letra(sigla)
    i = 0
    while i < len(vetor_sigla):
        if ord(vetor_sigla[i][0]) > 48 and ord(vetor_sigla[i][0]) <= 57:
            nova_sigla += vetor_sigla[i - 1] * (int(vetor_sigla[i]) - 1)
        else:
            nova_sigla += vetor_sigla[i]
        
        i += 1
    
    return nova_sigla


def separa_num_letra(string):
    vetor = []
    valor = ""
    i = 0
    while i < len(string):
        if ord(string[i]) >= 65 and ord(string[i]) <= 122:
            if valor != "":
                vetor.append(valor)
                valor = ""
            vetor.append(string[i])
            
        else:
            valor += string[i]
        i += 1   
    if valor != "":
        vetor.append(valor)
    return vetor

def separa_letras(string):
    lista = []
    i = 1
    qnt = 1
    while i < len(string):
        if string[i] == string[i - 1]:
            qnt += 1
        else:
            lista.append(string[i - 1] * qnt)
            qnt = 1
        i += 1
    lista.append(string[i - 1] * qnt)
    
    return lista
    
def compacta_string(string):
    nova_string = ""
    lista_string = separa_letras(string)
    for i in lista_string:
        nova_string += i[0] + str(i.count(i[0]))
    return nova_string

palavra = input("Digite uma palavra: ")

print(compacta_string(palavra))

print(descompacta("bs10e"))

#print(separa_num_letra("c3a2bs4d3"))
