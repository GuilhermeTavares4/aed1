import random as rd

jogadap1=input(f"Qual é a sua jogada? ")
jogadap2=rd.randint(0,2)
if jogadap2 == 0:
	jogadap2 = "pedra"
else:
	if jogadap2 == 1:
		jogadap2 = "papel"
	else:
		jogadap2 = "tesoura"

if (jogadap1 != "pedra" and jogadap1 != "papel" and jogadap1 != "tesoura"):
	print("Erro. Jogada inválida.")
else:

	if jogadap1 == jogadap2:
		print(f"Houve um empate! O bot jogou {jogadap2} também!")
	else:
		if jogadap1 == "pedra":
			if jogadap2 == "tesoura":
				print(f"Você venceu! O bot jogou {jogadap2}.")
			else:
				print(f"O bot venceu! Ele jogou {jogadap2}.")
		else:
			if jogadap1 == "papel":
				if jogadap2 == "pedra":
					print(f"Você venceu! O bot jogou {jogadap2}.")
				else:
					print(f"O bot venceu! Ele jogou {jogadap2}.")
			else:	
				if jogadap2 == "papel":
					print(f"Você venceu! O bot jogou {jogadap2}.")
				else:
					print(f"O bot venceu! Ele jogou {jogadap2}.")

