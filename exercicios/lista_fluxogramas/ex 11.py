notaTrab = float(input("Digite a nota do trabalho: "))
notaProva = float(input("Digite a nota da prova: "))
media = (notaTrab + notaProva * 3) / 4
if media >= 7:
    print(f"O aluno passou com a nota {media}.")
else:
    print("O aluno está em exame.")
