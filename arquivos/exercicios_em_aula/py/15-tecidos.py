import os.path

def read_tecidos(arq_estoque):
    if not os.path.exists(caminho + arq_estoque):
        print('arquivo naoe xiste vai se foder')
        return False
    
    with open(caminho + arq_estoque, 'r') as arq:
        tecidos = arq.read()
        tecidos = tecidos.splitlines()
        for i in range(len(tecidos)):
            tecidos[i] = tecidos[i].split(";")
            tecidos[i][2] = int(tecidos[i][2])
            tecidos[i][3] = int(tecidos[i][3])
    return tecidos    


def write_tecidos(tecidos):
    if tecidos == False:
        return
    with open(caminho + '15-estoque_50metros.txt', 'w') as arq:
        tecidos_menor_50m = ""
        for tecido in tecidos:
            if tecido[3] <= 50:
                tecidos_menor_50m += tecido[0] + ";" + str(tecido[3]) + "\n"
        arq.write(tecidos_menor_50m)

    with open(caminho + '15-estoque_15reais.txt', 'w') as arq:
        tecidos_menor_15reais = ""
        for tecido in tecidos:
            if tecido[2] <= 15:
                tecidos_menor_15reais += tecido[0] + ";" + str(tecido[2]) + "\n"
        arq.write(tecidos_menor_15reais)


caminho = 'txt/'
write_tecidos(read_tecidos('15-estoque.txt'))
    

