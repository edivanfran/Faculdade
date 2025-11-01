import random
n_lista = []
for i in range(10):
    n_lista.append(random.randint(1, 100))
soma = 0
print(n_lista)
for i, v in enumerate(n_lista):
    if i % 2 == 0:
        soma += v
print(soma)
