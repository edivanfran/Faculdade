
def primo(numero: int) -> bool:
    if numero % 2 != 0 and numero % numero == 0 or numero == 2 or not (numero < 2): 
        return True
    else:
        return False
def eh_primo(num):
    if num <= 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

sao_primos = []
nao_primos = []

try:
    numero = int(input("Digite um número: "))
    if numero < 0:
        quit()
except:
    print("Erro ao converter.")
for num in range(1, numero+1):
    if primo(num):
        sao_primos.append(num)
    else:
        nao_primos.append(num)
print(f"Lista com primos: {sao_primos}\n Lista sem primos: {nao_primos}")

