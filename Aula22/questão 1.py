def divide(a, b):
    if b == 0:
        raise ValueError("Parâmetro inválido.")
    # if b == 0:
    #     raise ZeroDivisionError("Tentativa de divisão por zero.")

    return a / b

print(divide(10, 0))