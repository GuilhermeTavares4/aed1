f = float(input("Digite uma temperatura em Farenheit: "))
cAprox = (f - 30) / 2
cExato = (f - 32) / 1.8
if abs(cAprox - cExato) > 4:
    print("O valor aproximado se difere em mais de 4 graus em relação ao valor exato")
else:
    print("Não difere em mais de 4 graus.")