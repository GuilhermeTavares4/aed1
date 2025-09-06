salBruto = float(input("Digite o salário bruto: "))
inss = salBruto * .08
ir = salBruto * .1
fs = (salBruto - inss - ir) * .005
totalDescontos = inss + ir + fs
salLiquido = salBruto - inss - ir - fs
print(f"Valor INSS: {inss} reais")
print(f"Valor IR: {ir} reais")
print(f"Valor filiação sincical: {fs} reais")
print(f"Valor total dos descontos: {totalDescontos} reais")
print(f"Salário líquido: {salLiquido} reais")
