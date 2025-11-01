import random
nu = random.randint(1, 100)
jogador = 0
while nu != jogador:
  jogador = int(input("Digite um número inteiro para tentar adivinhar o valor(0 à 100): "))
  if jogador > 100:
     print("O valor digitado é maior que 100! Não vale!")
  elif nu < jogador:
    print("O valor que foi digitado é Muito alto")
  elif nu > jogador:
    print("O valor que foi digitado é Muito baixo.") 

if nu == jogador :
    print("Você ganhou.")

