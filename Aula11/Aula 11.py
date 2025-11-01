tupla = (1, 2, 3, [1, 2 , 37], 7 )
tuplanho = (1, 2, 3, [1,3, 5, 8, 18], 8)
tuplanho[3].append(7)
print(tuplanho)
print(tupla.index(3))

lista = [0, 1, 4, 5, 6, 1, 2, 7, 3]
lista.sort()
print(lista)
n1, n2, n3, n4, n5, n6, n7, n8, n9 = lista
print(n5)

l1  = [1, 2, 3, 4]
l2 = [6, 7, 8, 9]

for a, b, in zip (l1, l2):
    print(a + b)