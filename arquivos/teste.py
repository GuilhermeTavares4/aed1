with open ('./texto.txt', 'r') as arq:
    conteudo = arq.read(5)
    arq.seek(2, 0)
    conteudo2 = arq.read()
    print(conteudo)
    print("------------------------")
    print(conteudo2)