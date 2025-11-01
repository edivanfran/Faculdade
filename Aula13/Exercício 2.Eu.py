entrada = """01/01/2025 Pix para Joãozinho -50,00
#02/01/2025 Pix para Mariazinha -30,00
#03/01/2025 Recebimento de salário 1.000,00
#03/01/2025 Gasolina -200,00
#04/01/2025 Hambúrguer sebosão -40,00"""
linhas = entrada.split("\n")
valores = 0
for linha in linhas:
    completo = linha.split(" ")
    numero = completo[-1]
    numero = numero.replace(".", "").replace(",", ".")
    valores += float(numero)
saldo = str(valores).replace(".", ",")
saldo = saldo + "0" if saldo.endswith(",0") else saldo
print(saldo)