

contagem = 0

try:
    arquivo1 = open("arquivo1.txt", "w")
    arquivo1.write("Testando alterando a primeira linha.\n")
    arquivo1.writelines(["Testando alterar\n", "Alterando linha 2\n", "alterando string", "7"])
    while contagem < 10:
        arquivo1 = open("arquivo1.txt", "a")
        arquivo1.write("Escrevendo alguma coisa\n")
        contagem += 1
except:
    print("Falha na manipulação de arquivos")
finally:
    arquivo1.close()