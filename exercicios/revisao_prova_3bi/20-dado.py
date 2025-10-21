import random

def rolar_dado():
    return random.randint(1, 6)


lancamentos = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
}

for i in range(100):
    num = rolar_dado()
    lancamentos[str(num)] += 1

print(lancamentos)