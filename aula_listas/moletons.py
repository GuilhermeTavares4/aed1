nomes = []
tamanhos = []
precoMoletom = 135
nome = input("Digite o nome da pessoa: ")
tamanho = input("Digite o tamanho do moletom: ")
while nome != "":
    nomes.append(nome)
    tamanhos.append(tamanho)
    nome = input("Digite o nome da pessoa: ")
    tamanho = input("Digite o tamanho do moletom: ")
valorTotal = precoMoletom * len(nomes)
tamanhoEsp = input("Digite um tamanho específico de moletom: ")
while tamanhoEsp != "M" and tamanhoEsp != "G" and tamanhoEsp != "P" and tamanhoEsp != "PP" and tamanhoEsp != "GG":
    print("Tamanho inválido")
    tamanhoEsp = input("Digite o tamanho novamente: ")
else:
    i = 0
    tamanhoQnt = 0
    while i < len(tamanhos):
        if tamanhos[i] == tamanhoEsp:
            tamanhoQnt += 1
        i += 1
    nomeEsp = input("Digite um nome da lista: ")
    i = 0
    temNaLista = False
    while i < len(nomes):
        if nomes[i] == nomeEsp:
            temNaLista = True
            indiceNome = i
        i += 1
    tamanhoEspNomes = input("Digite um tamanho (parte 2): ")
    while tamanhoEspNomes != "M" and tamanhoEspNomes != "G" and tamanhoEspNomes != "P" and tamanhoEspNomes != "PP" and tamanhoEspNomes != "GG":
        print("Tamanho inválido (parte 2)")
        tamanhoEspNomes = input("Digite o tamanho novamente (parte 2): ")
    i = 0
    nomesEncomenda = []
    while i < len(tamanhos):
        if tamanhos[i] == tamanhoEspNomes:
            nomesEncomenda.append(nomes[i])
        i += 1
    print(f"O custo total de moletons é R${valorTotal}")
    if temNaLista == False:
        print(f"O nome '{nomeEsp}' não está na lista.")
    else:
        print(f"{nomeEsp} escolheu o tamanho {tamanhos[indiceNome]}.")
    print(f"Há {tamanhoQnt} moletons do tamanho {tamanhoEsp}.")
    nomesEncomendaText = ""
    i = 0
    while i < len(nomesEncomenda):
        nomesEncomendaText += f"{nomesEncomenda[i]}, "
        i += 1
    nomesEncomendaText = nomesEncomendaText[:-2]
    nomesEncomendaText += "."
    print(f"Pessoas que encomendaram o tamanho {tamanhoEspNomes}: {nomesEncomendaText}")

    
    html = "<html><head><meta charset='UTF-8'><title>Document</title></head><body>"
    html += "<table border='1' align='center' cellpadding='10'>"
    html += "<caption>Tabela dos moletons</caption>"
    html += "<tr><th>Nome</th><th>Tamanho</th></tr>"
    i = 0
    while i < len(nomes):
        html += f"<tr><td align='center'>{nomes[i]}</td><td align='center'>{tamanhos[i]}</td></tr>"
        i += 1
    html += "</table></body></html>"
    with open("./a.html", "w") as f:
        f.write(html)
