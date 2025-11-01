lista = []

while True:
    try:
        print("=-"*32)
        menu = int(input("""
    1. Cadastrar Funcionário
    2. Listar Todos os Funcionários
    3. Listar Funcionários por Cargo
    4. Média Salarial por Cargo
    5. Funcionário com Maior Salário
    6. Aumentar Salário por Nome
    7. Remover Funcionário por Nome
    8. Sair
    """))
        print("=-"*32)
        match menu:
            case 1:
                lista.append(
                    (
                    input("Digite o nome do funcionário: "),
                    input("Digite o cargo do funcionário: "),
                    float(input("Digite o salário do funcionário: "))
                    )
                )
            case 2:
                for funcionario in lista:
                    print(funcionario[0])
            case 3:
                cargo = input("Digite o cargo: ")
                for funcionario in lista:
                    if funcionario[1] == cargo:
                        print(funcionario[0])
            case 4:
                cargo = input("Digite o cargo que você deseja ver a média salarial: ")
                som = 0
                quantidade = 0
                for funcionario in lista:
                    if funcionario[1] == cargo:
                        som += funcionario[2]
                        quantidade += 1
                if som == 0:
                    print("Salário do cargo não encontrado.")
                else:
                    print(f"Média salárial é: {som/quantidade:.2f}")
            case 5:
                maior = 0
                funci_n = ""
                funci_c = ""
                for funcionario in lista:
                    if funcionario[2] > maior:
                        maior = funcionario[2]
                        funci = funcionario[0]
                        funci_c = funcionario[1]
                print(f"O funcionário com maior salário é {funci} com {maior}, cargo: {funci_c}.")
            case 6:
                nome = input("Digite o nome do usuário que você deseja encontrar: ")
                aumentar = float(input("Digite o percentual que você deseja aumentar o salário: "))/100
                achou = False
                for i,funcionario in enumerate(lista):
                    if nome == funcionario[0]:
                        novo_salario = funcionario[2] + funcionario[2] * aumentar 
                        nova_tupla = (funcionario[0], funcionario[1], novo_salario)
                        lista[i] = nova_tupla
                        achou = True
                        break
                if not achou:
                    print("Não encontrado o funcionário. ")
                else:
                    print(f"Valor atualizado. Salário novo: {novo_salario}")
            case 7:
                nome = input("Digite o nome do funcionário para desejar excluí:")
                achou = None
                for funcionario in lista:
                    if nome == funcionario[0]:
                        lista.remove(funcionario)
                        achou = True
                if not achou:
                    print("Funcionário não foi encontrado.")
                else:
                    print("Funcionário removido.")
            case 8:
                break
    except:
        print("Tente novamente.")
print("Programa encerrado.")
                