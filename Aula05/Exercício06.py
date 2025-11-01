dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

if 1<= dia <= 31 and 1 <= mes <= 12 and 1 <= ano < 2025 :
    print("Data válida")
else: 
    print("Data inválida.")