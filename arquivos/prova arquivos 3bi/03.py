cidades_por_estado = {}

with open('dados_ibge/cidades.csv', 'r') as file:
    next(file)
    cidades = file.read()
    cidades = cidades.splitlines()
    for i in range(len(cidades)):
        cidades[i] = cidades[i].split(';')
        if cidades[i][2] not in cidades_por_estado:
            cidades_por_estado[cidades[i][2]] = 1
        else:
            cidades_por_estado[cidades[i][2]] += 1

nome_mais_longo = max(cidades, key = lambda cidade: len(cidade[1]))
nome_mais_curto = min(cidades, key = lambda cidade: len(cidade[1]))

with open('dados_sumarizados.txt', 'w') as file:
    txt = 'Número de cidades por estado:\n'
    for key, value in cidades_por_estado.items():
        txt += f'{key}: {value}\n'
    txt += '----------------------------\n'
    txt += f'Cidade com nome mais longo: {nome_mais_longo[1]}\n'
    txt += f'Cidade com nome mais curto: {nome_mais_curto[1]}'
    file.write(txt)



     


