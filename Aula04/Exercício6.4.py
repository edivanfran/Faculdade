idade = int(input("Qual sua idade? \n"))
if 19 < idade < 69:
    print(idade)
else:
    print("Infelizmente, você não pode ser doador."); exit()
peso = float(input("Qual seu peso? \n"))
if peso >= 50:
    print(peso)
else :
    print("Infelizmente, você não pode ser doador."); exit()
tatuagem= (input("Você fez alguma tatuagem no último ano(VERDADEIRO ou FALSO)."))
if tatuagem == "FALSO":
    print(tatuagem)
else: 
    print("Infelizmente, você não pode ser doador."); exit()
álcool = (input("Você ingeriu álcool nas últimas 12 horas(VERDADEIRO ou FALSO)?"))
if álcool == "FALSO":
    print("Parabéns, você pode doar sangue.")
else:
    print("Infelizmente, você não pode ser doador."); exit()


