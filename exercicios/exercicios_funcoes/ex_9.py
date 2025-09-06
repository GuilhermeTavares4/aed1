
def verif_expressao_matematica(string):
    last_simbolo = ""
    for char in string:
        if char == ")" and last_simbolo not in parenteses:
            return False
        if char == "]" and last_simbolo != ")":
            return False
        if char == "}" and last_simbolo != "]":
            return False
        if char == "[" and last_simbolo != "{" and last_simbolo != "":
            return False 
        if char == "(" and last_simbolo not in parenteses and last_simbolo != "[" and last_simbolo != "":
            return False
        if char == "{" and last_simbolo != "":
            return False  

        if char in colchetes or char in chaves or char in parenteses:
            last_simbolo = char
    return True


colchetes = ["[", "]"]
chaves = ["{", "}"]
parenteses = ["(", ")"]

expressao = "{[()()]}"

if verif_expressao_matematica(expressao):
    print('é valida')
else:
    print("nao é valida")