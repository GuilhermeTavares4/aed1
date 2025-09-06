from datetime import date
data_nasc=input("Digite sua data de nascimento: ")
ano_nasc = int(data_nasc[6:10])
mes_nasc = int(data_nasc[3:5])
dia_nasc = int(data_nasc[0:2])
ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day
idade = ano_atual - ano_nasc
if mes_atual < mes_nasc or (mes_atual == mes_nasc and dia_atual < dia_nasc):
	idade -= 1
print(idade)
if idade < 16:
	print("Não pode votar")
else:
	if idade < 18 or idade >= 70:
		print("Voto facultativo")
	else:
		print("Voto obrigatório")
