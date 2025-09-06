altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo: ")
peso = float(input("Digite o peso: "))
if sexo == "masc":
    pesoIdeal = 72.7 * altura - 58
else:
    pesoIdeal = 62.1 * altura - 44.7
var_abs = peso - pesoIdeal
var_per = peso / pesoIdeal * 100
if var_per > 108:
    print("Peso elevado.")
else:
    if var_per < 92:
        print("Peso abaixo.")
    else:
        print("Peso normal.")