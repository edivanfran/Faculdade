nome = input("Digite seu nome: ")
horas = int(input("Que horas são? "))
genero = input("Você é homem ou mulher?(h/m) ")

if horas > 12:
    if genero == "h":
        print(f"Bom dia, Senhor {nome}. São {horas} horas") 
    else:
        print(f"Boa tarde, Senhor {nome}. São {horas} horas")

if horas > 12:
    if genero == "m" :
        print(f"Bom dia, Senhora {nome}. são {horas} horas")
    else:
        print(f"Boa tarde, Senhora {nome}. São {horas} horas")
print("Fim")