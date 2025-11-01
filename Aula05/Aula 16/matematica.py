def soma(a: float, b: float) -> float:
    """Essa função recebe dois floats e retorna a SOMA."""
    return a + b

def subtracao(a: float, b: float) -> float:
    """Essa função recebe dois floats e retorna a SUBTRAÇÃO."""
    return a - b

def multiplicacao(a: float, b: float) -> float:
    """Essa função recebe dois floats e retorna a MULTIPLICAÇÃO."""
    return a * b

def divisao(a: float, b: float) -> float:
    """Essa função recebe dois floats e retorna a DIVISÃO."""
    if b == 0.0:
        return "Divisão por zero não pode ser realizada."
    return a / b

def potencia(a: float, b: float) -> float:
    """Essa função recebe dois floats e retorna a POTÊNCIA."""
    return a ** b