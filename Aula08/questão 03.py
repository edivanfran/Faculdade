num = int(input("Digite um número positivo inteiro: "))

fatorial = 1
while num > 0:
    fatorial *= num
    num -= 1
        
print(fatorial)

