try:
    dicionario = {"nome": "", "idade":"","maior de idade":""}
    dicionario = {"nome":input("Digite o nome do aluno: "), 
                  "idade":int(input("Digite a idade do aluno: ")),
    "maior de idade":""}

    if int(dicionario["idade"]) >= 18:
        print("O aluno é maior de idade.")
        dicionario["maior de idade"] = True
    else:
        print("O aluno não é maior de idade.")
        dicionario["maior de idade"] = False
    
    print(dicionario)
    # ou
    dicionario["maior de idade"] = dicionario["idade"] >= 18
    print(dicionario)
except:
    print("Erro ao converter")