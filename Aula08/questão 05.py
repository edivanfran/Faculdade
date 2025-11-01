numero = input("Digite um número positivo interio: ")
maior, menor = 0, 9
for digito in numero:
    digito = (int(digito))
    if digito >= maior:
        maior = digito
    if digito <= menor:
        menor = digito
print(f"O maior digitado: {maior}, o menor digitado: {menor}")