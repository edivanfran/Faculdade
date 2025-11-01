contador, primeiro, maior, menor = 0, True, 0, 0

while contador < 5:
    num = float(input(f"Digite algum número: "))
    if primeiro:
        maior = num
        menor = num
        primeiro = False
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    contador += 1
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")