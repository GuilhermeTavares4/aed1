texto = ""
with open("exercicios_em_aula/txt/07-juntar_conteudo_1.txt", "r") as arq1, open("exercicios_em_aula/txt/07-juntar_conteudo_2.txt", "r") as arq2:
    texto = arq1.read() + arq2.read()

with open("exercicios_em_aula/txt/07-juntar_conteudo_novo.txt", "w") as arq:
    arq.write(texto)
    