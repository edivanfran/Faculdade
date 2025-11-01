calculadora, mens = True, True
while calculadora:
    numero1 = float(input("Digite um número a ser calculado: "))
    numero2 = float(input("Digite outro número a ser calculado: "))
    operador = (input("Digite um operador (+, -, /, *): "))

    if operador == "+" :
        print(f"A soma é: {numero1 + numero2}")
    elif operador == "-":
        print(f"A subtração é: {numero1 - numero2}")
    elif operador == "*":
        print(f"A multiplicação é: {numero1 * numero2}")
    elif numero2 == 0 :
        print("Não é possível realizar divisão por zero")
    elif operador == "/" :
        print(f"A divisão é: {numero1 / numero2}")
    else:
        print("Operador é inválido.")
    while mens: 
        mens = input("Deseja continuar? S/N.")
        if mens == "N":
            mens, calculadora = False, False
            print("Obrigado pelo uso.")
        elif mens == "S":
            break
        else: 
            print("Digite outro dentro das opções.")

