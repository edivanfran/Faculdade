lista = []

def cadastrar_motorista(nome, data, cnh):
    


def verificar_data(data: str) -> str:
    data = " ".join(data.split()).strip()
    data_lista = data.split("/")

    try:
        dia, mes, ano = int(data_lista[0]), int(data_lista[1]), int(data_lista[2])
    except ValueError:
        raise ValueError("Erro ao converter")
    
    if  0 > dia > 31:
        raise ValueError("Dia inválido")
    
    if 0 > mes > 12:
        raise ValueError("Mês inválido")
    
    if 0 > ano > 2025:
        raise ValueError("Ano inválido")
    
    if ano < 2007 and mes < 7 and dia < 21:
        raise ValueError("Menor de idade")
    
    return "ok"
    
def maior_idade(data):
    data = " ".join(data.split()).strip()
    data_lista = data.split("/")

    dia, mes, ano = int(data_lista[0]), int(data_lista[1]), int(data_lista[2])

    