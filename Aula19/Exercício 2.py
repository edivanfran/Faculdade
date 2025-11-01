try:
    valor = int(input("Digite um valor do divisor: "))
    print(30/valor)
except ValueError:
    print("Erro: Valor digitado não é um int")
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except Exception as e:
    print("Error: infelizmente um erro aconteceu.", e)
except KeyboardInterrupt:
    print("Programa interrompido.")
else:
    print("Fim do programa.")
