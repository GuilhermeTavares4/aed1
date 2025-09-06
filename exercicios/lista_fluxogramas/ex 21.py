preco = float(input("Digite o preço do produto: "))
formaPagamento = input("Digite a forma de pagamento (à vista ou parcelado): ")
if (formaPagamento == "à vista"):
    valorPagar = preco * .9
    comissao = valorPagar * .005
    print(f"Valor total a pagar: R${valorPagar}")
else:
    valorParcela = preco / 3
    comissao = preco * .007
    print(f"Valor da parcela: R${valorParcela}")
print(f"Valor da comissão: R${comissao}")