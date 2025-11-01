numero = range(10, 101, 2)
print(list(numero))

for i in range(5):
  print(i) #imprime números de 0 a 4

contador = 0

while contador < 101:
 print(contador)
 contador += 1

contador = 0
while contador < 101:
 if contador % 2 == 0:
    print(contador)
 contador += 1

primo = 0

nome = "Edivan"

for letra in nome:
 print(letra) # imprime cada letra em uma linha.

pala = input("Digite uma palavra:")