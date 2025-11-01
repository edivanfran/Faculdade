lista = []
while True:
    try:
        valores = input("Digite um número inteiro, digite 'x' para sair: ")
        if valores.lower().strip() == "x":
            break
        lista.append(int(valores))
    except:
        print("Valor inválido. Erro ao converter o número.") 
tupla = tuple(lista)
print("A quantidade que o 5 aparece na tupla: ", tupla.count(5))

if 3 in tupla: # reduzindo para não usar o for.
    tupla.index(3)
    print("A posição do primeiro número 3.",tupla.index(3))
else:
    print("Não tem número 3 em tupla.")
maior = []
for i in tupla: # print(i for i in tupla if i > 10)
    if i > 10:
        maior.append(i)
if maior == []:
    print("Não tem nenhum valor maior que 10.")
else:
    print("Todos os números maiores que 10 presentes na tupla.", maior)