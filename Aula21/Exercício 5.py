from modulo5 import *

try:
    with open(r"C:\Users\junin\Downloads\teste-20250726T190408Z-1-001\Aula 21\lista.txt", "r") as varia:
        texto = varia.readlines()
        for linha in texto:
            linha = linha.replace("\n", "")
            lista_com_dados = linha.split(";")
            lista_com_dados.pop(0)
            for dado in lista_com_dados:
                if dado not in dicionario.keys(): 
                    dicionario[dado] = 1
                else:
                    dicionario[dado] += 1

    print(maior_aluno_com_faltas())
except FileNotFoundError:
    print("Erro na manipulagem do arquivo.")
except Exception as e:
    print("Erro:", e)
    
