import os.path

def get_nomes(arq_nomes, arq_notas):
    if not os.path.exists(caminho + arq_nomes):
        print('arquivo naoe xiste vai se foder')
        return
    
    with open(caminho + arq_nomes, 'r') as arq:
        nomes = arq.read()
        nomes = nomes.splitlines()
        for nome in nomes:
            aluno = {
                "nome": nome,
            }
            alunos.append(aluno)
    get_notas(arq_notas)


def get_notas(arq_notas):
    if not os.path.exists(caminho + arq_notas):
        print('arquivo naoe xiste vai se foder')
        return
    
    with open(caminho + arq_notas, 'r') as arq:
        todas_notas = arq.read()
        todas_notas = todas_notas.splitlines()
        for i in range(len(todas_notas)): 
            notas_individuais = todas_notas[i].split()
            for j in range(len(notas_individuais)):
                notas_individuais[j] = int(notas_individuais[j])
            alunos[i]["notas"] = notas_individuais


def gera_arquivo_medias(arq_medias):
    with open(caminho + arq_medias, 'w') as arq:
        texto = ""
        for aluno in alunos:
            linha = aluno["nome"] + ";"
            soma = 0
            for nota in aluno["notas"]:
                soma += nota
            media = soma / len(aluno["notas"])
            linha += str(media)
            linha += "\n"
            texto += linha
        arq.write(texto)


caminho = 'txt/'
alunos = []
get_nomes('13-nomes.txt', '13-notas.txt')
gera_arquivo_medias('13-medias.txt')
print(alunos)
