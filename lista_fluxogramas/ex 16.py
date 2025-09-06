import math
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o termo constante: "))
delta = (b ** 2) - 4 * a * c
raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Raiz 1: {raiz1}. Raiz 2: {raiz2}")