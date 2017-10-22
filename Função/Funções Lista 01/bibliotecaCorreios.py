def validaTipoItem(tipo):
    if tipo == "PACOTE" or tipo == "DOCUMENTO":
        return True
    else:
        return False

def validaPeso(peso):
    if peso >= 0:
        return True
    else:
        return False

def convertePeso(peso):
    res = peso*1000
    return res

def calculaCustoItem(tipo,peso):
    if tipo == "PACOTE":
        peso_kilo = 1000/3
        peso_final = peso/peso_kilo
        return peso_final
    elif tipo == "DOCUMENTO":
        peso_kilo = 1000/2
        peso_final = peso/peso_kilo
        return peso_final
    else:
        return "Tipo inválido!"

def validaEmbalagem(tamanho):
    if tamanho == "pequena":
        return True
    elif tamanho == "média":
        return True
    elif tamanho == "grande":
        return True
    else:
        return False

def calculaCustoEmbalagem(tamanho):
    if tamanho == "pequena":
        valor = 4
        return valor
    elif tamanho == "média":
        valor = 7
        return valor
    elif tamanho == "grande":
        valor = 10
        return valor
    else:
        return "Tipo inválido!"

def validaEntrega(entrega):
    if entrega == "normal":
        return True
    elif entrega == "sedex":
        return True
    elif entrega == "sedex 10":
        return True
    else:
        return False

def calculaCustoEntrega(tipo):
    if tipo == "normal":
        valor = 0
        return valor
    elif tipo == "sedex":
        valor = 5
        return valor
    elif tipo == "sedex 10":
        valor = 8
        return valor
    else:
        return "Tipo Inválido!"
