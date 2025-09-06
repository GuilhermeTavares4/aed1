def conversor_sigla(nome):
    vetor_nome = nome.split()
    sigla = ""
    i = 0
    while i < len(vetor_nome):
        if vetor_nome[i] not in conectivos:
            sigla += vetor_nome[i][0]
        i += 1
            
    return sigla

def sigla_numero(sigla):
    nova_sigla = ""
    i = 1
    cont = 1
    while i < len(sigla):
        if sigla[i] == sigla[i - 1]:
            cont += 1
        else:
            nova_sigla += sigla[i - 1]
            if cont > 1:
                nova_sigla += str(cont)
            cont = 1
        i += 1
    nova_sigla += sigla[i - 1]
    if cont > 1:
        nova_sigla += str(cont)
    return nova_sigla

conectivos = ("de", "da", "do")

nome = input("Digite seu nome: ")

print(conversor_sigla(nome))
print(sigla_numero(conversor_sigla(nome)))