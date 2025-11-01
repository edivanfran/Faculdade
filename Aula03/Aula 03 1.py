nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1+nota2)/2 >= 6 and (nota1 != 0 and nota2 !=0)
print(media)

aprovado = (((nota1 + nota2)/2) >= 6) and (nota1 != 0 and nota2 !=0)
print(aprovado)

print(f"Aprovado? {aprovado}")