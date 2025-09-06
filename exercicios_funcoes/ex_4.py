def verif_espaco(string):
    for i in string:
        if i == " ":
            return False
    return True

def verif_qnt(string):
    if len(string) < 8:
        return False
    return True

def verif_caracteres(string):
    tem_letra_mai = False
    tem_letra_min = False
    tem_num = False
    for char in string:
        if ord(char) >=  65 and ord(char) <= 90:
            tem_letra_mai = True
        else:
            if ord(char) >= 97 and ord(char) <= 122:
                tem_letra_min = True
            else:
                if ord(char) >= 48 and ord(char) <= 57:
                    tem_num = True

    if not tem_letra_mai or not tem_letra_min or not tem_num:
        return False
    return True

def verif_senha(senha):
    if verif_espaco(senha) and verif_qnt(senha) and verif_caracteres(senha):
        return True
    return False

senha = input("Digite uma senha: ")

if verif_senha(senha):
    print("É uma senha válida.")
else:
    print("É uma senha inválida.")
