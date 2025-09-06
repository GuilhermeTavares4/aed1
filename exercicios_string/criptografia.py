def criptografa(nome, passo):
    nome_list = list(nome)
    nome_novo = ""
    for i in nome_list:
        valor_ascii = ord(i)        
        valor_novo = (((valor_ascii - 65) + passo) % 26) + 65
        nome_novo += chr(valor_novo)
    return nome_novo

print(criptografa("JOSEZ", 2))
    