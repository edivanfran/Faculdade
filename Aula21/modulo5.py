dicionario = {}

def maior_aluno_com_faltas():
    maior = ["a", 0]
    for aluno, faltas in dicionario.items():
        if faltas > maior[1]:
            maior = [aluno, faltas]
    
    return maior