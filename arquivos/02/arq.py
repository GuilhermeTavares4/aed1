from pathlib import Path

filepath = Path(__file__).parent / "arq.txt"

num = int(input("Digite um número: "))


len_tabuada = 10

tabuada = ''

i = 0
while i <= len_tabuada:
    mult = num * i
    tabuada += f'{num} x {i} = {mult}\n'    
    i += 1
with open(filepath, 'w') as arq:
    arq.write(tabuada)
    