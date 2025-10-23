turma = []

nomes = ['braian', 'braian', 'erik', 'guilherme']
notas = [[9.9, 9.4], 9.3, 9.8, 9.7]

for nome, nota in zip(nomes, notas):
    turma.append({
        'nome': nome,
        'nota': nota
    })
media = 0
# for aluno in turma:
#     media += aluno['nota']

media = media / len(turma)
print(media)
print(turma)
nome = input('Digite um nome:')
notas = [aluno['nota'] for aluno in turma if aluno['nome'] == nome]

for i in range(len(notas)):
    if type(notas[i]) is list:
        notas[i] = sum(notas[i]) / len(notas[i])

print(f'{nome}s:  {notas}')
