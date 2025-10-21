def byte_to_mebibyte(bytes):
    return bytes / 1048576


def porcentagem(valor, total):
    return valor / total * 100


with open('19-usuarios.txt', 'r') as arq:
    linhas = arq.read()
    linhas = linhas.splitlines()
    info = list(map(lambda linha: [linha[:15].strip(), byte_to_mebibyte(int(linha[15:]))], linhas)) #feio pra caralho
    total = sum(map(lambda usuario: usuario[1], info))
    for pessoa in info:
        pessoa.append(porcentagem(pessoa[1], total))

with open('19-relatorio.txt', 'w', encoding='UTF-8') as arq:
    texto = "Furg             Uso do espaço em disco pelos usuários\n"
    texto += "------------------------------------------------------------------------\n"
    texto += f"Nr. Usuário{19 * ' '}Espaço utilizado{13 * ' '}% do uso\n\n"
    for i, pessoa in enumerate(info):
        linha = ""
        linha += f"{i + 1}  {pessoa[0]}"
        linha += (30 - len(linha)) * " "
        linha += f"{pessoa[1]:.2f} MB"
        linha += (59 - len(linha)) * " "
        linha += f"{pessoa[2]:.2f}%\n"
        texto += linha
    arq.write(texto)