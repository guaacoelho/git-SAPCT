def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

# ola tudo bem?
def potencia(a, pot):
    return a ** pot

def multiplicacao(a, b):
    return a * b

# aqui a gente divide
def divisao(a, b):
    if b == 0:
        raise Exception("Não pode dividir por zero")
    return a / b