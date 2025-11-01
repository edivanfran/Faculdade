from questao_modulos import *

while True: 
    try:
        menu  = int(input("Digite uma opção dentro das opções: \n1. Cadastrar o aluno \n2. Calcular média das notas do aluno \n3. Buscar um aluno pelo nome \n4. Exibir todos os alunos. \n5. Sair.\n"))
    except:
        print("Digite apenas NÚMEROS.")
        continue
    match menu:
        case 1:
            nome = input("Digite o nome do aluno: ").strip()
            if not verificador_nome(nome)[0]:
                print(verificador_nome(nome)[1])
                continue

            idade = input(f"Digite a idade de {nome}: ")
            ok, mensagem = verificador_idade(idade)
            if not ok:
                print(mensagem)
                continue

            notas = []
            for i in range(3):
                nota = input(f"Digite a {i+1}° nota: ").strip()
                if nota == "" or not (nota.replace(".", "").isdigit()) or nota.count(".") > 1:
                    print("Digite só números.")
                    break
                if nota.endswith(".0") or not nota.isalpha():
                    nota = float(nota)
                if nota < 0:
                    print("Erro: Nota negativa.")
                    break
                if nota > 10:
                    print("Erro: Nota maior que 10.")
                    break
                notas.append(nota)
            notas = tuple(notas)

            cadastro = cadastro_aluno(nome, idade, notas)
            print(cadastro[1]) 
        case 2:
            nome = "".join(input("Digite o nome do aluno: ").split()).strip()
            print(calcular_media(nome)[1])
        case 3:
            nome = "".join(input("Digite o nome do aluno que deseja buscar: ").split()).strip()
            print(buscar_alunos(nome)[1])
        case 4:
            if alunos:
                for aluno in alunos:
                    print(aluno)
            else:
                print("Dicionário vazio.")
        case 5:
            break
        case _:
            print("Digite um número dentro das opções.")

print("Programa encerrado.")