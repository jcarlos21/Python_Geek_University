"""
Questão 37
"""


def hiperfatorial(x):
    H = 1
    for i in range(1, x + 1):
        H *= i ** i
    return H


num = int(input('Entre com um número inteiro: '))
print(f'O superfatorial de {num} é: {hiperfatorial(num)}')
