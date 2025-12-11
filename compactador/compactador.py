import os

def compacta(filepath):
    if not os.path.exists(filepath):
        print("O arquivo não existe.")
        return
    with open (filepath, 'r', encoding='UTF-8') as arq:
        palavras_txt = []
        for linha in arq.readlines():
            palavras_txt += linha.split(' ')
        dicionario_palavras = {}
        posicoes = []
        pos = 0
        for palavra in palavras_txt:
            if palavra not in dicionario_palavras:
                dicionario_palavras[palavra] = pos
                pos += 1
            posicoes.append(str(dicionario_palavras[palavra]))
        palavras_string = ''
        for palavra in dicionario_palavras.keys():
            palavras_string += palavra
            if '\n' not in palavra:
                palavras_string += ' '
    posicoes_string = " ".join(posicoes)
    with open('texto_compactado.gui', 'w', encoding='UTF-8') as arq:
        texto = palavras_string
        if texto[-1] != '\n':
            texto += '\n'
        texto += posicoes_string
        arq.write(texto)


filepath = input('Digite o nome do arquivo para compactar: ')
compacta(filepath)