alunos = []

def verificador_nome(nome: str) -> tuple:
    if nome.isdigit():
        return (False, "Erro: digite apenas letras.")    
    elif nome == "":
        return (False, "Erro: digite alguma coisa")
    return (True, "Informações corretamente colocadas.")

def verificador_idade(idade: str) -> tuple:
    if not idade.isdigit():
        return (False, "Erro: Idade inválido.")
    
    idade = int(idade)

    if idade < 1:
        return (False, "Erro: Digite uma idade maior que 1")
    elif idade > 122:
        return (False, "Erro: Digite uma idade maior de 122. Esse é o recorde mundial.")
    return (True, "Informação corretamente colocada.")

def cadastro_aluno(nome: str, idade: int, notas: tuple) -> tuple:
    for dicionario in alunos:
        if nome in dicionario.values():
            return (False, "Erro: Aluno já cadastrado.")
        
    if len(notas) != 3:
        return (False, "Erro: Notas não totalmente cadastradas.")
    
    alunos.append({"nome":nome, "idade": idade, "notas": notas})
    return (True, "Cadastrado com sucesso.")

def buscar_alunos(nome: str) -> tuple:
    for dicionario in alunos:
        if nome in dicionario.values():
            return (True, dicionario)
    return (False, "Aluno não encontrado")

def calcular_media(nome:str) -> tuple:
    for dicionario in alunos:
        if nome in dicionario.values():
            return (True, sum(dicionario["notas"]) / len(dicionario["notas"]))
    return (False, "Aluno não encontrado")
