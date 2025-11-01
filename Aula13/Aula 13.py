var = "Ednaldo"
print(var[2:-1])

valor_1 = "A"
valor_2 = "a"
ver = valor_1 < valor_2
print(valor_1.replace("A", "a"))
print(ver)

# Exercício
nome = input("Digite um nome: ")
nome_2 = input("Digite outro nome: ")

print("Os strings são iguais" if input("Digite um nome: ") == input("Digite outro nome: ") else "Os strings são diferentes")
if nome == nome_2:
    print("Os strings são iguas")
else:
    print("Os strings são diferentes")
print(nome)
print(nome_2)