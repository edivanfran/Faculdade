### import matematica
from utilitarios.matematica import soma, sub, mult # Para todas as pastas você tem que colocar  a pasta
# from matematica import * Assim usa para importa tudo que tá lá dentro
from random import randint
# from matematica import soma as add Para renomear
import utilitarios.matematica as m # Para deixar um módulo com outro nome

# print(add(5, 10))
print(m.sub(9, 3))

print(soma(1, 12))
print(sub(4, 2))
print(mult(4, 5))
print(randint(1, 100))