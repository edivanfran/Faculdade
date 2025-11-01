idade, menor, adulto, idoso = [], 0, 0, 0
try:
    for i in range(10):
        idade.append(int(input("Digite uma idade: ")))
    for i in idade:
        idade_verif = idade.pop()
        if (idade_verif < 18):
            menor += 1
        elif (18 <= idade_verif) and (idade_verif <= 59):
            adulto += 1
        elif idade_verif >= 60:
            idoso += 1
    print(f"Existem na lista. Menor de 18 anos: {menor}, Adulto: {adulto}, Idoso: {idoso}")
except:
    print("Erro ao converter")