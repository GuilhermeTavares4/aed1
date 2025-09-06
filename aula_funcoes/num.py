def faz(num, limite):
    if(num > limite):
        return print('vai toma no seu cu')
    print(f'oi {num}')
    if (num < limite):
        faz(num + 1, limite)
    print(f'tchau {num}')
    

faz(20, 50)