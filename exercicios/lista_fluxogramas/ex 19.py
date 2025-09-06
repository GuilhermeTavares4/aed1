notaTrab1 = float(input("Digite a nota do primeiro trabalho: "))
notaProva1 = float(input("Digite a nota da primeira prova: "))
notaTrab2 = float(input("Digite a nota do segundo trabalho: "))
notaProva2 = float(input("Digite a nota da segunda prova: "))
media = (((notaTrab1 + notaProva1 * 3) / 4) + ((notaTrab2 + notaProva2 * 3) / 4)) / 2
if media >= 7:
    print(f"O aluno obteve uma média maior ou igual a sete.")
else:
    print(f"O aluno não obteve uma média maior ou igual a sete.")
print(media)