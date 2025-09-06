def add_voto():
    candidato = ""
    votos = []
    candidatos = []
    while candidato != "fim":
            candidato = input("Digite o número do seu candidato: ")
            if candidato != "fim":
                if candidato not in candidatos:
                    candidatos.append(candidato)
                    votos.append(1)
                else:
                    votos[candidatos.index(candidato)] += 1
    maior_voto = max(votos)
    maior_candidato = candidatos[votos.index(maior_voto)]

    return maior_candidato


def verif_candidato(num):
    if len(num) < 2 or len(num) > 6:
        return False
    return True


print("O maior candidato é: " + add_voto())

#if verif_is_num("123"):
 #    print("fodase")