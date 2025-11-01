# Tratamento de Exceções:



* Exceções são situações anormais na execução que sem tratamento acarretam na interrupção precoce do programa.
* Não confundir com erros de sintaxe, com esses erros o **programa não é executado**.



print(10/0) # ZeroDivisionError

Ele LANÇA UMA exceção.

print("O programa não chega aqui!")



print(x) # NameError, o "x" NÃO foi definida anteriormente ou não foi atribuída.



Ao tratar o erro, nós queremos que o erro apareça de uma forma amigável.



Tipos Comuns de Exceção em Python.

* ZeroDivisionError: divisão por zero.
* ValueError: entrada inválida para conversão.
* IndexError: índice inexistente dentro de uma lista.
* KeyError: chave inexistente em dicionários. (Quando você não usa o get)
* FileNotFoundError: arquivo não encontrado.
* TypeError: operações em tipo de dado incompatível. (Funciona muito com str + int)



Tipos Comuns de Exceção em Python

* Principais palavras reservadas utilizadas para tratamento de erros:
* try -> bloco no qual está o código que é verificado.
* except -> bloco no qual o erro é tratado.
* else -> bloco executado quando não acontece nenhum erro. (Opcional)
* finally -> bloco executado independente de te acontecido algum erro ou não.



try:

&nbsp;	print(x)

except:

print("infelizmente tivemos um problema, tente novamente mais tarde") #Dá um NameError. Porém, além da mensagem o código ainda é executado. (Para deixar o usuário com lágrima)



Você pode especificar qual vai ser o erro ao lado do except.



try:

&nbsp;	valor = int(input("Digite o divisor: "))

&nbsp;	print(10/valor)

except ValueError:

&nbsp;	print("Falha ao converter!")

finally:

&nbsp;	print("Terminou o programa!")



Quando você coloca um except sem nada ele sempre cai nele se nem um outro erro não foi executado anteriormente.



Como:

try:

&nbsp;	valor = int(input("Digite o divisor: "))

&nbsp;	print(10/ valor)

&nbsp;	print(y)

except ValueError: 

&nbsp;	print("Não foi possível converter o valor digitado para inteiro.")

except ZeroDivisionError:

&nbsp;	print("Divisão por zero.")

except: # Essa boa prática serve para quando você não sabe quais erros apareceram no programa

&nbsp;	print("Algum erro aconteceu")



Finally, é mais usado para fechar o arquivo, então dando um erro ou não, vai ser executado.

O else serve apenas se nenhuma exceção for levantada.



Raise você pode focar o lançamento de exceções através do uso da palavra raise.

Utilizar o raise(lançar) tem o mesmo efeito de uma exceção ser lançada, ou seja, o fluxo do programa é alterado e pode ser tratado. A gente lança essa exceção antes da erro.



Uma função também pode lançar um erro. A função não retorna nada, ela lança um ZeroDivisionError.

O raise tem que ser seguido de uma exceção.



def dividir(a, b):

&nbsp;	if b == 0:

&nbsp;		raise ZeroDivisionError("Tentativa de divisão por zero")

&nbsp;	return a/b



try:

&nbsp;	print(dividir(10,0))

except ZeroDivisionError as zde:

&nbsp;	print(zde)



opção, você pode colocar um try dentro da função ou raise para retornar o erro.

O Raise é só para break o programa mais bonito.























