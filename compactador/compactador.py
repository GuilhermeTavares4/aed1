def compacta(filepath):
    with open ('texto.txt', 'r', encoding='UTF-8') as arq:
        palavras_txt = []
        for linha in arq.readlines():
            palavras_txt += linha.split(' ')
        palavras_filtradas = []
        posicoes = []
        for palavra in palavras_txt:
            if palavra not in palavras_filtradas:
                palavras_filtradas.append(palavra)
            posicoes.append(str(palavras_filtradas.index(palavra)))
        palavras_string = ''
        for palavra in palavras_filtradas:
            palavras_string += palavra
            if '\n' not in palavra:
                palavras_string += ' '
    posicoes_string = " ".join(posicoes)
    with open('texto_compactado.txt', 'w', encoding='UTF-8') as arq:
        texto = palavras_string
        if texto[-1] != '\n':
            texto += '\n'
        texto += posicoes_string
        arq.write(texto)



compacta('a')