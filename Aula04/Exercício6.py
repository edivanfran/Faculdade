print("Informe as medidas do três lados.")
numero1 = int(input("Digite um lado: "))
numero2 = int(input("Digite outro lado: "))
numero3 = int(input("Digite algum lado: "))
print(numero1)
print(numero2)
print(numero3) 

if numero1 == numero2 == numero3:
    print("Trata-se de um triângulo equilátero")
elif numero1 == numero2 or numero1 == numero2 or numero3 == numero2:
    print("Trata-se de um triângulo isósceles.")
else:
    print("Trata-se de um triângulo escaleno.")
