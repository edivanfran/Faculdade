lista = []

def cadastrar_livro(titulo:str, autor:str, ano:int, avaliacao_notas:tuple):
    titulo = " ".join(titulo.split(" ")).strip() # O split aqui é vazio, split()
    autor = " ".join(autor.split(" ")).strip() 
    lista.append({"titulo": titulo, "autor": autor, "ano_publicacao": ano, "avaliacoes": avaliacao_notas})
    return "Livro cadastrado."

def verificador_digitou_alguma_coisa(texto:str) -> tuple:
    if texto == "":
        return (False, "Erro: Digite alguma coisa.")
    return (True, "ok")

def verificador_ano(ano:str) -> tuple:
    if ano == "":
        return (False, "Erro: Digite algum número.")
    try:
        ano = int(ano)
    except:
        return (False, "Erro: Digite só números. Ex: 2025")
    if ano < 0:
        return(False, "Erro: Ano negativo.")
    if ano > 2025:
        return(False, "Erro: Ano superior ao atual.")
    return (True, "ok")

def verificador_avaliacao(avaliacoes:list) -> tuple:
    for nota in avaliacoes:
        try:
            nota = float(nota)
        except:
            return (False, "Erro: Digite só números. Ex: 10")
        if nota < 0:
            return (False, "Erro: Nota negativa.")
        if nota > 10:
            return (False, "Erro: Nota maior que 10.")
    return (True, "ok")

def tupla_avaliacoes(avaliacoes: list) -> tuple:
    notas = []
    for nota in avaliacoes:
        nota = int(nota) # Era para ter deixado float.
        notas.append(nota)
    return tuple(notas)


def calcular_media(titulo:str) -> int:
    for livro in lista:
        if titulo.lower() == livro["titulo"].lower():
            if livro:
                return sum(livro["avaliacoes"])/len(livro["avaliacoes"])
    return 

def buscar_livro(titulo:str) -> dict:
    for livro in lista:
        if titulo.lower() == livro["titulo"].lower():
            return livro 
    return 

