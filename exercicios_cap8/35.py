"""
Questão 35
"""


def fatorial(x):
    fat = 1
    for i in range(1, x + 1):
        fat *= i
    return fat


def fatorialquadruplo(x):
    return fatorial(2 * x) / fatorial(x)


num = int(input('Entre com um número inteiro: '))
print(f'O fatorial quádruplo de {num} é: {fatorialquadruplo(num)}')
