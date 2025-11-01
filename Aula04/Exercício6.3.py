quilometros = float(input("Quantos quilômetros o carro percorre por litros? \n"))
litros = float(input("Quantos litros tem no carro atualmente? \n"))
distância = float(input("Qual distância (em Km) você deseja percorrer ? \n"))

per = quilometros * litros
neces = distância - per
fal = neces / quilometros

if fal > 0:
    print(f"Você precisa abastecer {fal} litros")
else:
    print("Você não precisa abastecer")