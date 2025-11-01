def media(listinha):
    return sum(listinha)/len(listinha)

lista = []
while True:
    try:
        entrada = float(input("Digite o número que você quer: "))
        if entrada < 0:
            print("Menor que zero.")
            continue
    except:
        print("Erro ao converter.")
    lista.append(entrada)
    continuar = input("Deseja continuar? Digite 'x' para sair: ").strip().lower()
    if continuar == "x":
        break

print(media(lista))

# Args

def media(*args):
    return sum(*args)/len(*args)

lista = []
while True:
    try:
        entrada = float(input("Digite o número que você quer: "))
        if entrada < 0:
            print("Menor que zero.")
            continue
    except:
        print("Erro ao converter.")
    lista.append(entrada)
    continuar = input("Deseja continuar? Digite 'x' para sair: ").strip().lower()
    if continuar == "x":
        break

print(media(*lista))

