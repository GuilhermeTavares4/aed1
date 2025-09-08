def palindromo(string):
    if len(string) == 0:
        return "True"

    if string[0] != string[-1]:
        return False
    
    return palindromo(string[1:-1])


def format_string(string):
    string_nova = ""
    for i in string:
        if i != " " and i != "-":
            string_nova += i
    string_nova = string_nova.lower()

    return string_nova


string = "Socorram-me subi no onibus em Marrocos"
print(palindromo(format_string(string)))
