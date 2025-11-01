lista_num, impares, posi = [], [], []
try:
    for i in range(10):
            lista_num.append(int(input("Digite um número inteiro:")))
    contador = 0
    for i, v in enumerate(lista_num):
        if v % 2 == 0:
            contador += 1
    for i, v in enumerate(lista_num):
        if v % 2 == 1:
            impares.append(v)
            posi.append(i)
    print(f"Quantas vezes os números pares aparecem na lista: {contador}, Números ímpares: {impares} e sua posição {posi}.")
except:
    print("Error ao converter.")