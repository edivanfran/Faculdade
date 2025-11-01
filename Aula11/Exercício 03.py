# Chance alta de cair em prova #
# Sistema de supermercado
produto = []
compra, preco = [], []
# produto, preco = (), ()
for i in range(5):
    try:
        prod = (input("Digite o produto que você quer registrar: "), float(input("Digite o preço do produto: ")))
        produto.append(tuple(prod))
    except:
        print("Erro valor inválido.")
produto = (tuple(produto))
for rep in range(5): 
    print("Produto: ", produto[i], "Preço: ", produto[i,i+1])

soma = 0
while True:
    try: # Tentar usar com for,  S = 0, S += i[i]
        compra = input("Produto que você quer comprar e digite 'x' para finalizar: ")
        for i in range(5):
            if compra in produto[i,1]:
                soma += produto[i,1]
        if compra == 'x':
            break
    except:
        print("Erro ao converter.")
print(compra)



