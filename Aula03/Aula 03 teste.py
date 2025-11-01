num1, num2, num3 = int(input("Digite um número: ")), int(input("Digite algum número: ")), int(input("Digite outro número: "))
ordemcres = (num1 > num2 > num3)
ordemdesc = (num1 < num2 < num3)
print(ordemcres or ordemdesc)