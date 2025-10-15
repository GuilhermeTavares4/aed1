def count_char(char):
    with open("exercicios_em_aula/txt/03-total_char.txt", 'r') as arq:
        texto = arq.read()
        count_char = 0
        for i in texto:
            if i == char:
                count_char += 1
    return count_char


char = input("Digite um caractere: ")

print(f"Esse caractere aparece {count_char(char)} vezes no arquivo.")