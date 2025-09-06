def criptografa(string, num):
    nova_string = ""
    for i in string:
        novo_ord = 65 + ((ord(i) + num - 65) % 26)
        nova_string += chr(novo_ord)
    return nova_string

palavra = input("Digite uma palavra: ")
num = int(input("Digite um número: "))

print(criptografa(palavra, num))