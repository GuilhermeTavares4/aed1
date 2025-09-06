import random
random.seed()
num = random.randint(0, 100)
nTentativas = 10
chuteInt = None
chuteStr = None
while chuteInt != num and nTentativas > 1 and chuteStr != "love":
	if chuteInt:
		nTentativas -= 1
	chuteStr = (input(f"Digite um número. Você tem {nTentativas} tentativas: "))
	if (chuteStr != "love"):
		chuteInt = int(chuteStr)
		if chuteInt < num:
			print(f"Errou. O número é maior que {chuteInt}.")
		else:
			if chuteInt > num:
				print(f"Errou. O número é menor que {chuteInt}.")

if chuteStr == "love":
	print("Fracassado.")
else:
	if chuteInt != num:
		print(f"Você é o pior do mundo. O número era {num}.")
	else:
		print(f"Boa nerd, o número de fato era {chuteInt}.")