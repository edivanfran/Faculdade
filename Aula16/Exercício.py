import matematica as math

while True:
    num1 = ""
    num2 = ""
    try:
        num1 = float(input("Digite o 1° número para operação: "))
        num2 = float(input("Digite o 2° número para operação: "))
    except:
        print("Digite apenas números.")
    if not (num1 == "" or num2 == ""):
        operador = int(input("""Digite qual operação quer fazer? 
1. Soma 
2. Subtração 3. Multiplicação 4. Divisão 5. Potência \n"""))
        match operador:
            case 1:
                print(math.soma(num1, num2))
            case 2:
                print(math.subtracao(num1, num2))
            case 3:
                print(math.multiplicacao(num1, num2))
            case 4:
                print(math.divisao(num1, num2))
            case 5:
                print(math.potencia(num1, num2))
            case _:
                print("Digite uma opção")

    continuar = input("Deseja continuar? Digite 'x' para sair: ").strip()

    if continuar.lower() == "x":
        break
print("Programa pe")