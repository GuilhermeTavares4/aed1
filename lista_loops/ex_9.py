alfabeto = "abcdefghijklmnopqrstuvwxyz"
string = input("Digite uma string: ")
i = 0
letraCont = 0
while i < len(string):
    j = 0
    while j < len(alfabeto):
        if string[i] == alfabeto[j]:
            letraCont += 1
        j += 1
    i += 1
if letraCont == len(string):
    print("É formada apenas por letras.")
else:
    print("Não é formada apenas por letras.")
