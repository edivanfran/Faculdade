# Calculadora
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um outro número: "))
operador = input("Digite só um: (+, -, *, /) ")

resultado = True
resultado = resultado and (operador == "+") and (numero1 + numero2)
resultado = not resultado and (operador == "-") and (numero1 - numero2)
resultado = not resultado and (operador == "/") and (numero1 / numero2)
resultado = not resultado and (operador == "*") and (numero1 * numero2)

print(resultado)

# exercício - Ano Bissexto
ano = int(input("Digite um ano: "))
ano = ((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0)
print(f"É ano bissexto: {ano}")

# Par ou Ímpar
numero = int(input("Digite um número: "))
numero = (numero % 2) == 0 and "Par" or (numero % 2) != 0 and "Ímpar"
print("O número é:", numero)

