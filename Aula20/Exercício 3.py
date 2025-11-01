from random import randint

while True:
    try:
        menu = int(input("Digite uma dessas opções: \n1. Cadastrar novo motorista \n2. Listar motoristas \n3. Sair\n "))
    except ValueError:
        print("Digite só números.")

    match menu:
        case 1:
            nome = input("Digite o nome do motorista: ")

            data_nascimento = input("Digite a data de nascimento nesse modelo (DD/MM/AAAA): ")

            cnh = randint(10000000000,)

            
        