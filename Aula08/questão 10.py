dia, mes, ano = "", "", ""
while True:
    data1, data_ok = "", True
    data = input("Digite uma data válida: (DD/MM/AAAA) ")
    for valido in data:  
        if valido in "0123456789":
            data1 += valido

    if len(data1) >= 5:
        dia = int(data1[:2])
        mes = int(data1[2:4])
        ano = int(data1[4:])

    if not (1 <= ano <= 2025):  
        data_ok = False
    elif not (1 <= mes <= 12):
        data_ok = False
    elif mes == 2 and not(1 <= dia <= 28):
        data_ok = False
    elif ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and not(1 <= dia <= 30)):
         data_ok = False
    if data_ok:
        print("Data válida.")
        print(f"A data é: Dia:{dia}, Mês:{mes}, Ano: {ano}")
        break  
    else:
        print("Data inválida, tente novamente.")
    