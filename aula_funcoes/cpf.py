def validadorCPF(cpf):
    dv1 = 0
    dv2 = 0
    if len(cpf) != 11:
        return False
    i = 0
    peso = 10
    soma = 0
    while i < len(cpf) - 2:
        soma += int(cpf[i]) * peso
        i += 1
        peso -= 1
    if soma % 11 == 0 or soma % 11 == 1:
        dv1 = 0
    else:
        dv1 = 11 - (soma % 11)
    i = 0
    peso = 11
    soma = 0
    while i < len(cpf) - 2:
        soma += int(cpf[i]) * peso
        i += 1
        peso -= 1
    soma += dv1 * peso
    if soma % 11 == 0 or soma % 11 == 1:
        dv2 = 0
    else:
        dv2 = 11 - (soma % 11)

    if int(cpf[9]) != dv1 or  int(cpf[10]) != dv2:
        return False
    return True

cpf = input("Digite um CPF: ")

if validadorCPF(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")