lista = []

for num in range(101):
    lista.append(num)
print(lista)

print(i for i in range(0, 101))
print(i*2 for i in range (0, 101, 2))

print(int(input("Digite um número: ") for i in range(11)))
lista = [i for i in range(20) if i % 2 == 0]
lista = [i**2 for i in range(0, 20, 2)]

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista3 = lista1 + lista2
print(lista1 + lista2)

lista = [0 * 10]
print(lista)