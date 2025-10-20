def sequencia_em_branco(string):
    maior_sequencia = 0
    sequencia = 0
    i = 0
    for char in string:
        if char != " ":
            sequencia = 0
        else:
            sequencia += 1
            if sequencia > maior_sequencia:
                maior_sequencia = sequencia
    return maior_sequencia


string = "     5espacosesmbrancoatras          10espacosembrancologoatrase6espacosembrancoàfrente      "

print(sequencia_em_branco(string))