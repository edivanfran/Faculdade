nome = input("Digite seu nome: ")
hora = int(input("Que hora são? "))
genero = input("Digite qual é seu gênero?(m/f) ")

if hora < 12:
    cumprimento = "Bom dia"
elif hora > 18 :
        cumprimento = "Boa tarde"

if genero == "m":
    pronome = "Senhor"
else:
    pronome = "Senhora"

print(f"{cumprimento}, {pronome} {nome}. São {hora} horas.")
print("Fim")