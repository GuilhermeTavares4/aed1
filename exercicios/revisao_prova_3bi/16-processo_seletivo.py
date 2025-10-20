with open('16-processo_seletivo.txt') as arq:
    cursos = arq.read()
    cursos = cursos.splitlines()
    for i in range(len(cursos)):
        cursos[i] = cursos[i].split(";")
        for j in range(2, len(cursos[i])):
            cursos[i][j] = int(cursos[i][j])
    total_candidatos = 0
    for curso in cursos:
        total_candidatos += curso[3] + curso[4]
        candidatos_por_vaga = (curso[3] + curso[4]) / curso[2]
        print(f'codigo: {curso[1]}; candidatos por vaga: {candidatos_por_vaga}; porcentagem de candidatos do sexo feminino: {curso[4] / (curso[3] + curso[4]) * 100}%')
        
    print(max(cursos, key=lambda x: (x[3] + x[4]) / x[2]))
    print(total_candidatos)