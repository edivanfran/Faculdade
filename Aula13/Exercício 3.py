nome = "Edivan Francisco da Silva Junior"
nome = input("Digite seu nome: ")
partes = nome.split(" ")
nome_com_asteriscos = ""

primeiro_e_ultimo = " ".join([partes[0], partes[-1]])

for letra in primeiro_e_ultimo.lower():
    if letra in "aeiouAEIOU":
        nome_com_asteriscos += "*"
    else:
        nome_com_asteriscos += letra
print(nome_com_asteriscos)

nome_vogal = ["", ""]
for i, v in enumerate(partes):
    nome_vogal[i] = v.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*").replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")
print(" ".join(nome_vogal))