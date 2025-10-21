meses = ['janeiro', 'fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro', 'dezembro']
temps = []
for mes in meses:
    temp = float(input(f"Digite a temperatura média de {mes}: "))
    temps.append(temp)
temp_media_anual = 0
for temp in temps:
    temp_media_anual += temp

temp_media_anual = temp_media_anual / len(temps)
temps_acima_media = []
for i, temp in enumerate(temps):
    if temp > temp_media_anual:
        temps_acima_media.append([temp, i])
print(temp_media_anual)
for temp in temps_acima_media:
    print(f'{meses[temp[1]]}: {temp[0]}')
    
