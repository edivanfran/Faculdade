try:
    arquivo = open("arquivo.txt", "r")
    linhas = arquivo.readlines() 
    arquivo_novo = open("arquivo_novo1.txt", "w")
    arquivo_novo.writelines(linhas)
except:
    print("Erro na manipulação de arquivo.")
finally:
    arquivo.close()
    arquivo_novo.close()


import os
os.makedirs(r"C:\Users\ifpb\Desktop\Prova 3 - Ed", exist_ok=True)
print(os.path.exists("arquivo.txt"))

import shutil