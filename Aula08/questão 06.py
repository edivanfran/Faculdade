numero = int(input("Digite um número inteiro positivo: "))

for contagem in range(numero, -1, -1):
    print(contagem)
    if contagem == 0:
        print("Feliz ano novo!")
while numero >= 0:
    print(numero)
    numero -= 1