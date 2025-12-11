with open('dados_ibge/cidades.csv', 'r') as file:
    next(file)
    cidades = file.read()
    cidades = cidades.splitlines()
    for i in range(len(cidades)):
        cidades[i] = cidades[i].split(';')

with open('dados_ibge/estados.csv', 'r') as file:
    next(file)
    estados = file.read()
    estados = estados.splitlines()
    for i in range(len(estados)):
        estados[i] = estados[i].split(';')

for estado in estados:
    with open('cidades_estados/cidades_' + estado[0] + '.csv', 'w') as file:
        file_text = ''
        for cidade in cidades:
            if cidade[2] == estado[0]:
                line = ''
                line += cidade[1]
                line += '\n'
                file_text += line
        file.write(file_text)



