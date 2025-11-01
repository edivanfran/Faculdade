from modulo1 import maior_ou_igual_a_zero

try:
    num = int(input("Digite um número para verificar se é maior ou igual a zero: "))
except NameError:
    print("Error ao converter para inteiro.")
except ValueError:
    print("Erro o valor inserido não é um int. Ex: a")
except:
    print("Erro: infelizmente ocorreu um erro, tente novamente.")
else:
    print(maior_ou_igual_a_zero(num))

try:
    numero = int(input("Digite um número divisor: "))
    print(10/numero)
except ValueError:
    print("Falha na divisão do valor")
except:
    print("Falha inesperada")
else:
    print("Cálculo executado com sucesso!")
finally:
    print("Fim do tratamento de exceção")

print("Fim do programa!")