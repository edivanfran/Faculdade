num, maior = [], []
try:
    for i in range(10):
        num.append(int(input("Digite um número: ")))
    media = (sum(num)/10)
    print(f"Média: {sum(num)/10}")
    for i in range(10):
        numero = num.pop()
        if numero > media:
            maior.append(numero)
    print(f"Os números maiores que a média: {maior}")
except:
    print("Erro ao converter o valor.")

