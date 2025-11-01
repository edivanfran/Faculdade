num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

ve = not((num1 > 0) and (num2 > 0)) and ((num1 < 1) or (num2 < 1))
print("Existe algum número positivo e outro negativo? ",ve) 