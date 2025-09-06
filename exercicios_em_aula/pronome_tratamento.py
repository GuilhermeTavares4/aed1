nomeCompleto = input("Digite seu nome completo: ")
pronomeTratamento = input("Digite seu pronome de tratamento: ")
nome = ""
sobrenome = ""
i = 0
while nomeCompleto[i] != " ":
    nome += nomeCompleto[i]
    i += 1
i += 1
while i < len(nomeCompleto):
    sobrenome += nomeCompleto[i]
    i += 1

print(f"{pronomeTratamento} {sobrenome.upper()}, {nome}")