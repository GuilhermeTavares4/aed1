from pathlib import Path

#tira vogal e salva no arquivo 'arq_sem_vogal'
filepath = Path(__file__).parent / "arq.txt"

txt = ''
with open(filepath, 'r') as arq:
    txt = arq.read()

vogais = ['a','e','i','o','u','A','E','I','O','U', 'ã', 'õ', 'é', 'í', 'ó', 'ú', 'Ã', 'Õ', 'Á', 'É', 'Í', 'Ó', 'Ú']    
txt_novo = ''
for char in txt:
    if char not in vogais:
        txt_novo += char

filepath = Path(__file__).parent / "arq_sem_vogal.txt"
    
with open(filepath, 'w') as arq_novo:
    arq_novo.write(txt_novo)


#verifica se tem palavrao
txt = txt.split()
palavroes = ['PORRA', 'porra', 'CARALHO', 'caralho', 'PUTA', 'puta', 'BOSTA', 'bosta', 'MERDA', 'merda', 'CU', 'cu', 'LEAGUE', 'OF', 'LEGENDS', 'league', 'of', 'legends', 'LOL', 'lol']
simbolos = ['.', ',', '\n', ':', ';', '(', ')']
tem_palavrao = False
palavroes_encontrados = []
txt_censurado = ''
i = 0
while i < len(txt):
    palavra_temp = ''
    for char in txt[i]:
        if char not in simbolos:
            palavra_temp += char
    if palavra_temp in palavroes:
        for j in txt[i]:
            if j in palavra_temp:
                txt_censurado += '*'
            else:
                txt_censurado += j
        tem_palavrao = True
        if palavra_temp not in palavroes_encontrados:
            palavroes_encontrados.append(palavra_temp)
    else:
        txt_censurado += txt[i]
    txt_censurado += " "
    i += 1

filepath = Path(__file__).parent / "arq_censurado.txt"
    
with open(filepath, 'w') as arq_novo:
    arq_novo.write(txt_censurado)

if tem_palavrao:
    print('O arquivo contém palavras feias.')
    print(f'Lista das palavras feias: {palavroes_encontrados}')
else:
    print('O arquivo não contém certas palavras feias e certamente não fala de league of legends.')