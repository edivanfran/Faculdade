n = int(input("Digite um número inteiro: "))
restos1, reverso  = 0, 0

while n > 0:
    restos1 = n % 10
    reverso = reverso * 10 + restos1
    n = n // 10
print(reverso) 

# for não tem o problema com zero, transforma com string para int
valor = ""
for digito in n:
    valor += digito