def cont_vogais_unicas(string):
    vogais = ["a", "e", "i", "o", "u"]
    vogais_utilizadas = []
    cont_vogais = 0
    for char in string:
        if char in vogais and char not in vogais_utilizadas:
            vogais_utilizadas.append(char)
            cont_vogais += 1
    
    return cont_vogais


string = "breno de info"
print(f"Essa string tem {cont_vogais_unicas(string)} vogais distintas.")