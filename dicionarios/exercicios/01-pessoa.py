def aniversario(idade):
    return idade + 1


pessoa = {
    'nome': 'guilherme',
    'idade': 21,
    'cidade': 'rio grande',
    'cor favorita': 'roxo'
}

chave = input('Digite qual informação você quer saber dessa pessoa: ')

if chave not in pessoa:
    print('vai te foder magrao nao temos essa informacao')
else:
    print(pessoa[chave])

profissao = input('Digite a profissao dessa pessoa: ')

pessoa['profissão'] = profissao 
print(pessoa)

pessoa['idade'] = aniversario(pessoa['idade'])
print(pessoa['idade'])

pessoa.pop('profissão')
print(pessoa)

pessoa['cidade'] = 'cassino'
print(pessoa)
del pessoa['nome']
print(pessoa)


# coisas = {
#     'riogrande': 210000,
#     'pelotas': 330000,
#     'sao jose do norte': 28000,
#     'aao jose do nortaaaae': 28000
# }

# max_habitantes = max(coisas.items(), key = lambda x: len(x[0]))

# print(max_habitantes)