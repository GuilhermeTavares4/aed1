def add_alunos(nome, matricula, nota1, nota2, nota3):
    with open('exercicios_em_aula/txt/08-alunos.txt', 'a') as arq:
        aluno = {
            'nome': nome,
            'matricula': matricula,
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3
        }
        alunos.append(aluno)
        texto = ""
        for value in aluno.values():
            texto += f"{value}="
        texto = texto[:-1]
        texto += "\n"
        arq.write(texto)

    
with open('exercicios_em_aula/txt/08-alunos.txt', 'w') as arq:
    arq.write("")

alunos = []
num_alunos = int(input("Quantidade de alunos a inserir: "))

for i in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    nota1 = float(input("Nota 1 bi: "))
    nota2 = float(input("Nota 2 bi: "))
    nota3 = float(input("Nota 3 bi: "))
    add_alunos(nome, matricula, nota1, nota2, nota3)

with open("exercicios_em_aula/txt/08-alunos.txt", 'r') as arq:
    linhas = arq.readlines()
    for i in range(len(alunos)):
        media = (alunos[i]["nota1"] + alunos[i]["nota2"] + alunos[i]["nota3"]) / 3
        if media >= 7:
            situacao = "APROVADO"
        else:
            situacao = "REPROVADO"
        print(f"{linhas[i]}    {situacao} !!!!!!!!")
        print("\n")
