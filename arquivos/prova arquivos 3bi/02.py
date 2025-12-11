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
            
for city in searched_cities:
    print(city[1])
