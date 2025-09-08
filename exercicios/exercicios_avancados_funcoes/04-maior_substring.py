def maior_substring_unica(string):
    substring_final = ""
    substring_atual = ""
    lista_chars_encontrados = []
    for i in string:
        if i in lista_chars_encontrados:
            if len(substring_atual) > len(substring_final):
                substring_final = substring_atual
            substring_atual = i
            lista_chars_encontrados = [i]
        else:
            substring_atual += i
            lista_chars_encontrados.append(i)

    if len(substring_atual) >= len(substring_final):
                substring_final = substring_atual

    return substring_final


string = "abcabcfgbb"
print(maior_substring_unica(string))