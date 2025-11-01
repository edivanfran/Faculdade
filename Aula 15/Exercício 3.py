def verifica_hora(valor):
    if (valor[0:2]).isdigit() and (valor[3:5]).isdigit():
        horas = int(entrada[0:2])
        minutos = int(entrada[3:5])
    else:
        return "Digite HH:MM" 
    if 25 <= horas < 0 or 60 <= minutos < 0 or len(entrada) < 5:
        return
    if horas > 12:
        horas = horas - 12

while True:
    entrada = input("Digite um horário: ").strip()
    verifica_hora(entrada)
    print(f"{horas}:{minutos} P.M" if hora_maior else f"{horas}:{minutos} A.M")
    
        