tupla = (1, 4, "python", 9, "teste")
for i, v in enumerate(tupla):
    print(v)
for i in tupla:
    print(i)

lista = []
while True:
    valores = input("Digite um valor (x para parar)")
    if valores.lower().strip() == "x":
        break
    lista.append(valores)

tupla = tuple(lista)
print(tupla)