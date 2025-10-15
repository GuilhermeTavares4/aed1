with open("exercicios_em_aula/txt/01-qntas_linhas.txt", 'r') as arq:
    texto = arq.read()
    qnt_linhas = texto.count("\n")

print(qnt_linhas)