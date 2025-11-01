entrada = " ".join(input("Digite um texto: ").split()).strip()
dicionario = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
contador = {}

for letra in entrada:
    if letra.lower() in dicionario: # Vamos refazer depois fazendo isso, não é tão recomendad
        dicionario[letra.lower()] += 1
print(dicionario)

# for letra in entrada:
#     if letra == " ":
#         continue
#     contador[(letra.upper())] = contador.get(letra.upper(), 0) + 1

# for letra in entrada:
#     if letra == " ":
#         continue
#     if letra in contador:
#         contador[letra] += 1
#     else:
#         contador[letra] = 1
# print(contador)
