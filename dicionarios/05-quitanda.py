feira = {
    'batata':
    {
        'preco': 5,
        'qnt': 10
    },

    'tomate':
    {
        'preco': 3,
        'qnt': 15
    },

    'cenoura':
    {
        'preco': 2,
        'qnt': 5
    },
}

valor_total = 0

while True:
    item = input('Digite um item para comprar: ')
    if item == 'fecha':
        break
    if item not in feira:
        print('esse produto nao existe 🖕')
        continue
    if feira[item]['qnt'] == 0:
        print('nao tem mais no estoque 🖕')
        continue

    feira[item]['qnt'] -= 1
    valor_total += feira[item]['preco']
    print(f'voce comprou uma unidade de {item}! seu bolso esta esvaziando 😃')

print(feira)
print(valor_total)
