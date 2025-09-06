c=float(input("Digite o comprimento do retângulo (metros): "))
l=float(input("Digite a largura do retângulo (metros também): "))
if (c <= 0 or l <= 0):
	print("Apenas valores positivos.")
else:
	a = c * l
	p = 2 * (c + l)
	print(f"A área do retângulo é {a} metros quadrados e o perímetro é {p} metros.")


