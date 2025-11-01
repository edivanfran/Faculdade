import senha

try:
    tamanho = int(input("Digite o tamanho da senha: "))
except:
    print("Digite uma quantidade só em número.")
    
if tamanho < 1:
    print("Tamanho menor que 1.")

print(senha.gerar_senha(tamanho))
print(senha.gerar_senha_garantido(tamanho)[0:((tamanho))])

