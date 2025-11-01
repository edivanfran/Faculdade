# exercício 1
num = int(input("Digite um número: "))
ver = "É Par" if ((num % 2) == 0) else "É ímpar"
print(f"O número é: {ver}")

# exercício 2
horário = input("Qual é o horário que você estuda? \n M-matutino \n V-Vespertino \n N-Noturno \n")
if horário == "M":
    print("Bom Dia!")
elif horário == "V":
    print("Boa tarde!")
elif horário == "N":
    print("Boa noite!")
else :
    print("Valor Inválido")


# Exercício 3
nota1 = int(input("Digite sua primeiria nota parcial: "))
nota2 = int(input("Digite sua segunda note parcial: "))
média = (nota1 + nota2) / 2
# O importante da prova tem que da Valor Inválido se for número negativo

if média < 0:
    print("Valor inválido")
else:
    if 9.0 <= média <= 10.0:
        conceito = "A"
        print("APROVADO")
    elif 7.5 <= média <= 9.0:
        conceito = "B"
        print("APROVADO")
    elif 6.0 <= média <= 7.5:
        conceito = "C" 
        print("APROVADO")
    elif 4.0 <= média <= 6.0:
        conceito = "D"
        print("REPROVADO")
    elif  4.0 >= média >= 0.0:
        conceito = "E"
        print("REPROVADO")
    else:
        print("Valor inválido")

print(f"Notas: {nota1, nota2}, Média: {média}")

# Exercício 4
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
numero3 = int(input("Digite algum número inteiro: "))
maior = numero1
menor = numero1
if numero1 > numero2 > numero3 :
    print("O número 1 é o maior deles.")
elif numero2 > numero3 :
    print("O segundo é o maior deles")
elif numero3 > numero2 :
    print("O terceiro é o maior deles")
else:
    print("Existem números iguais")


