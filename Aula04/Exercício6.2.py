peso = float(input("Qual seu peso? "))
altura = float(input("Qual é a sua altura? "))

imc = (peso / altura **2)
print("Qual seu peso?")
print(peso)
print("Qual sua altura?")
print(altura)
print("IMC = ", imc)


if imc < 17:
    print("Muito abaixo do peso")
elif 17 < imc < 18.49:
    print("Abaixo do peso")
elif 18.5 < imc < 24.99: 
    print("Peso normal")
elif 25 < imc < 29.99:
    print("Acima do peso")
elif 30 < imc < 34.99 :
    print("Odesidade I")
if 35 < imc < 39.99 :
    print("Odesidade II(severa)")
elif imc > 40 : 
    print("Odesidade III(mórbida)")
   