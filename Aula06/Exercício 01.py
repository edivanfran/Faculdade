palavra = input("Digite qualquer palavra: ")
vogal = 0
for letra in palavra:
    print(letra)
    match letra:
        case "a" | "A" | "e" | "E" | "i" | "I"| "o" | "O" |"u" | "U":
            vogal += 1
    print("Existem: ", vogal, "vogais")


contador = 0
for letra in palavra:
    if letra in "aeiouAEIOUáãíé":
     contador += 1
print(f"A frase posuui {contador} vogais.")