def frequencia_cada_letra(texto):
    texto = list(texto)
    frequencia = {}
    for caracter in texto:
        if caracter == " " or caracter == ",":
            continue
        if caracter.lower() not in frequencia:
            frequencia[caracter.lower()] = 1
        else:
            frequencia[caracter.lower()]+= 1
    return frequencia