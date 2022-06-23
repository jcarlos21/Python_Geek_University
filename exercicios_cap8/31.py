"""
Questão 31
"""


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat


def neperiano(x):
    soma = 0
    for i in range(0, x+1):
        soma += (1 / fatorial(i))
    return soma


print(f'O neperiano para {1000} termos é: {neperiano(1000)}')
