numero = int(input("Digite um número inteiro menor que 1000: "))
centenas = numero // 100
resto = numero % 100
dezenas = resto // 10
unidades = resto % 10
print(f"Centenas: {centenas}, Dezenas: {dezenas}, Unidades: {unidades}")