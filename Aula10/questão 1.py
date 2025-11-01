lista1 = []
soma = 0
maior = 0
menor = 9
for i in range(5):
   lista1.append(int(input("Digite um número inteiro: ")))
  
for i, v in enumerate(lista1): 
    soma += v

    if maior < v:
        maior = v
    elif menor > v:
        menor = v
print(soma, lista1)
