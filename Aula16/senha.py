from random import randint
import string 

string_total = string.ascii_letters + string.digits + string.punctuation

def gerar_senha(tamanho):
    senha = ""
    for i in range(tamanho):
        senha = senha + string_total[randint(0, len(string_total) - 1)]
    return senha

def gerar_senha_garantido(tamanho):
    senha = ""
    for i in range(tamanho):
        senha = senha + string.ascii_letters[randint(0, len(string.ascii_letters) - 1)]
        senha = senha + string.digits[randint(0, len(string.digits) - 1)]
        senha = senha + string.punctuation[randint(0, len(string.punctuation) - 1 )]
    return senha