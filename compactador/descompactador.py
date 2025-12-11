def descompacta():
    with open('texto_compactado.gui', 'r', encoding='UTF-8') as arq:
        info = arq.readlines()
        palavras = []
        i = 0
        while i < len(info):
            info[i] = info[i].split(' ')
            
            i += 1
        for linha in info[: -1]:
            palavras += linha
            

        txt_descompactado = ''
        for pos in info[-1]:
            txt_descompactado += palavras[int(pos)]
            if txt_descompactado[-1] != '\n':
                txt_descompactado += ' '
        txt_descompactado = txt_descompactado[:-1]
    with open('texto_descompactado.txt', 'w', encoding='UTF-8') as arq:
        arq.write(txt_descompactado)


descompacta()