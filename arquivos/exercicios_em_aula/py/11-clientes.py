def add_cliente(nome, registro, compra1, compra2, compra3):
    cliente = {
        'nome': nome,
        'registro': registro,
        'compra1': compra1,
        'compra2': compra2,
        'compra3': compra3
    }
    clientes.append(cliente)


def write_clientes():
    with open('txt/11-clientes.txt', 'w') as arq:
        conteudo = ""
        for cliente in clientes:
            linha = ""
            for value in cliente.values():
                linha += str(value)
                linha += ";"
            linha = linha[:-1]
            
            linha += "\n"
            conteudo += linha
        arq.write(conteudo)


def read_clientes():
    with open('txt/11-clientes.txt', 'r') as arq:
        linhas = arq.readlines()
        for i in range(len(linhas)):
            texto = linhas[i][:-1]
            if clientes[i]['compra1'] + clientes[i]['compra2'] + clientes[i]['compra3'] > 1000:
                texto += " (VIP)"
            texto += "\n"
            print(texto)



clientes = []

add_cliente('guiherme', 1613, 300, 400, 500)                
add_cliente('breno', 1782, 300, 400, 200)                
add_cliente('breno2', 1439, 300, 400, 600)                

write_clientes()
read_clientes()