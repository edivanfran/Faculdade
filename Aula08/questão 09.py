divisor, numeros, soma, num = 0, "", 0, 0
while True:
  num = input("Digite um número, quando terminar digite 'x': ")
  if num == "x" or num == "X":
    break
  for digito in num:
    if digito not in "0123456789":
        valido = False
        break

    if valido:
      numero = int(num)
      soma += numero
      divisor += 1
    print("Digite novamente algum número ou 'x' para calcular a média dos números digitados.")
  numeros = int(numeros)
  soma += numeros
print(f"Média é: {soma / divisor}")