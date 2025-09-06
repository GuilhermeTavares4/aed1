import math
def verif_palindromo(string):
    index_i = 0
    index_f = len(string) - 1
    while index_i < math.ceil(len(string) / 2):
        if string[index_i] != string[index_f]:
            return False
        index_i += 1
        index_f -= 1
    return True

palavra = input("Digite uma palavra: ")

if verif_palindromo(palavra):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
