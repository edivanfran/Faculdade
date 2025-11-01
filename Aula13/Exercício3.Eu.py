nome = input("Digite seu nome: ").lower()
nome_separado = nome.split(" ")
primeiro_e_ultimo = nome_separado[0], nome_separado[-1]
nome_asterico = ""
for partes in primeiro_e_ultimo:
    for parte in partes: 
        if parte in "aeiouAEIOUáéíóúÁÉÍÓÚàâêîôû":
            nome_asterico += "*"
        else:
            nome_asterico += parte
    nome_asterico += " "
print(nome_asterico)