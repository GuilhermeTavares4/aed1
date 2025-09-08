def triangulo_pascal(n_linhas):
    linhas = []
    
    for index in range(n_linhas):
        linha = [1]
        if len(linhas) > 0:   
            for i in range(1, index):
                result = linhas[index - 1][i - 1] + linhas[index - 1][i]
                linha.append(result)
            linha.append(1)
        linhas.append(linha)

    return linhas


num = 6
print(triangulo_pascal(num))