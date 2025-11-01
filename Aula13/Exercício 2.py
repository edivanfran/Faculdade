entrada = """01/01/2025 Pix para Joãozinho -50,00
02/01/2025 Pix para Mariazinha -30,00
03/01/2025 Recebimento de salário 1.000,00
03/01/2025 Gasolina -200,00
04/01/2025 Hambúrguer sebosão -40,00"""
entrada = entrada.split("\n")
soma = 0
for i in entrada:
    elementos_linha = i.split(" ")
    valor_str = elementos_linha[-1].replace(".", "").replace(",", ".")
    valor = float(valor_str)
    soma += valor
resultado = str(soma)
resultado = resultado + "0" if resultado.endswith(",0") else resultado 
print(f"O saldo do indíviduo é: R$ {resultado.replace(".",",")}")