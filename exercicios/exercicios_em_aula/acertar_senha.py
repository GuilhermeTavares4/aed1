senha = "aed1_2025"
chute = input("digite a senha: ")
i = 10
while chute != senha and i > 1:
	print("Senha incorreta.")
	i -= 1
	chute = input(f"Digite a senha novamente. Tem mais {i} tentativas. ")
	
if i == 1:
	print("Errou.")
else:
	print("acertou.")
