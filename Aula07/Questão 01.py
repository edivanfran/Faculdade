while True:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    op = input("Digite o operador (+|-|*|/): ")

    match op:
        case "+":
            print(f"Soma: {n1 + n2}")
        case "-":
            print(f"Subtração: {n1 - n2}")
        case "/":
            if n2 != 0:
                print(f"Divisão: {n1 / n2}")
            else: 