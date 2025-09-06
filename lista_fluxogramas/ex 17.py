consumo = 14
velocidade = float(input("Digite a velocidade média: "))
tempo = float(input("Digite o tempo da viagem: "))
dist = velocidade * tempo
litros = dist / consumo
print(f"A distância percorrida é {dist}km. A quantidade de litros utilizada é {litros}l.")