a = float(input("Digite o lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo: "))
c = float(input("Digite o lado C do triângulo: "))
if a >= b + c or b >= a + c or c >= a + b or a <= 0 or b <= 0 or c <= 0:
    print("Triângulo inválido.")
else:
    if a == b and a == c:
        print("Triângulo equilátero.")
    else:
        if a == b or a == c or b == c:
            print("Triângulo isósceles.")
        else:
            print("Triângulo escaleno.")
