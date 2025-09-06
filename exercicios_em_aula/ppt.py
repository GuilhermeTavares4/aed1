jogador1=input("Digite o nome do jogador 1: ")
jogador2=input("Digite o nome do jogador 2: ")

jogadap1=input(f"Qual foi a jogada de {jogador1}? ")
jogadap2=input(f"Qual foi a jogada de {jogador2}? ")

if (jogadap1 != "pedra" and jogadap1 != "papel" and jogadap1 != "tesoura") or (jogadap2 != "pedra" and jogadap2 != "papel" and jogadap2 != "tesoura"):
	print("Erro. Jogada inválida.")
else:

	if jogadap1 == jogadap2:
		print("Houve um empate!")
	else:
		if jogadap1 == "pedra":
			if jogadap2 == "tesoura":
				print(f"{jogador1} venceu!")
			else:
				print(f"{jogador2} venceu!")
		else:
			if jogadap1 == "papel":
				if jogadap2 == "pedra":
					print(f"{jogador1} venceu!")
				else:
					print(f"{jogador2} venceu!")
			else:	
				if jogadap2 == "papel":
					print(f"{jogador1} venceu!")
				else:
					print(f"{jogador2} venceu!")
