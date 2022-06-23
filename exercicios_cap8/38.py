"""
Questão 38
"""


def fatorialexponencial(x):
    fte = 1
    for i in range(1, x+1):
        fte = i ** fte
    return fte


def Transcendental_Number(x):
    TransNumber = 0
    for i in range(1, x+1):
        TransNumber += 1 / fatorialexponencial(i)
    return TransNumber


num = int(input('Entre com um número inteiro: '))
print(f'O fatorial exponencial de {num}$ é: {fatorialexponencial(num)}')
print(f'O valor transcendental é: {Transcendental_Number(num)}')
