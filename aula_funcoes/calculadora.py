def calculadora(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        return x / y
    if op == "%":
        return x % y
    return "Operador ou valores inválidos"
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
op = input("Dgiitie o operador: ")
result = calculadora(n1, n2, op)
print(f"O resultado de {n1} {op} {n2} é {result}.")