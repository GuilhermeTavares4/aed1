def split(string, char = " "):
    lista_split = []
    string_temp = ""
    for i in range(len(string)):
        if string[i] != char:
            string_temp += string[i]
        else:
            if i != len(string) - 1:
                lista_split.append(string_temp)
                string_temp = ""
        
    lista_split.append(string_temp)

    return lista_split


string = "exemplo de frase para usar com split"
print(split(string, " "))