def gera_html(cities):
    html = "<html>\n<head>\n\t<meta charset='UTF-8'>\n\t<title>Cidades</title></head>\n<body>"
    html += "\n\t<table border='1' align='center' cellpadding='10'>"
    html += "\n\t\t<tr>\n\t\t\t<th>Cidade</th>\n\t\t\t<th>UF</th>\n\t\t</tr>"

    for city in cities:
        html += f"\n\t\t<tr>\n\t\t\t<td align='center'>{city[1]}</td>\n\t\t\t<td align='center'>{city[2]}</td>\n\t\t</tr>"

    html += "\n\t</table>\n\t</body>\n</html>"

    with open("cidades.html", "w") as file:
        file.write(html)


search_text = input('Digite um termo para busca: ')
searched_cities = []
with open('dados_ibge/cidades.csv', 'r') as file:
    next(file)
    cities = file.read()
    cities = cities.splitlines()
    for i in range(len(cities)):
        cities[i] = cities[i].split(';')
        if search_text in cities[i][1]:
            searched_cities.append(cities[i])

gera_html(searched_cities)

