valorPagamento = float(input("Digite o valor que o motorista pagou: "))
precoCombustivel = float(input("Digite o preço do combustível: "))
quantLitros = valorPagamento / precoCombustivel
print(f"O motorista conseguiu colocar {quantLitros} litros de combustível no tanque.")