lista = ()
salarios = 0

while True:
    try:
        print("-" * 7) 
        print("1. Cadastrar Funcionário \n2. Listar Todos os Funcionários \n3. Listar Funcionários por Cargo \n4. Média Salarial por Cargo \n5. Funcionário com Maior Salário \n6. Aumentar Salário por Nome \n7. Remover Funcionário por Nome \n8. Sair")
        menu = int(input("Digite algum número dentro das opções: \n"))
        match menu.strip():
            case "1":
                try:
                    pessoa = (
                        input("Digite o nome do funcionário: "), 
                        input("Digite o cargo do funcionário: "), 
                        float(input(f"Digite o salário: ")))
                    lista = list(lista)
                    lista.append(pessoa)
                    lista = tuple(lista)
                except:
                    print("Digite um salário válido.")
            case "2":
                if lista == ():
                    print("Lista vazia.")
                else:
                    for i in range(len(lista)):
                        print(lista[i][0][0])
                        print(lista)
            case "3":  
                if lista == ():
                    print("Lista vazia.")
                else:
                    for func in range(len(lista)):
                        if lista[func][2] == cargo:
                            por_fun = salario
                        print(cargo, por_fun)
            case "4": #da atenção
                salarios = 0
                if lista == ():
                    print("Lista vazia.")
                else:
                    for i, funci in enumerate(lista):
                        funci[1]
                        salarios += salario
                    else:
                        media = sum(salarios)/len(salarios)
                        print(media)
            case "5":
                maior = 0
                if lista == ():
                    print("Lista vazia.")
                else:
                    for funcio in lista:
                        if funcio[1] > maior:
                            maior = funcio[2]
                    print(f"O maior salário é {maior}")
            case "6":
                if lista == ():
                    print("Lista vazia.")
                else:
                    nome_aumentar = input("Digite o nome do funcionário que você deseja aumentar o salário.")
                    percentual = float(input("Digite o percentual: "))
                    achado = None
                    for funcio in lista:
                        if funcio[0] == nome_aumentar:
                            achado = funcio
                    if achado:


            case "7":
                try:
                    remover = ("Digite o funcionário que você deseja removor: ")
                    if remover in lista:
                        lista = list(lista)
                        lista.remove(remover)
                        lista = tuple(lista)
                    else:
                        print("Nome do funcionário não encontrado.")
                except:
                    print("Digite um nome válido.")
            case "8":
                break
            case _ :
                print("Digite uma opção válida.")
    except:
        print("Tente novamente.")  #Pode tirar os try de dentro
print("programa encerrado.")