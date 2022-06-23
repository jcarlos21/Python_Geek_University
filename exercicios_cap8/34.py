"""
Questão 34
"""


def fatorialduplo(x):
    fat = 1
    for i in range(1, x+1):
        if not i % 2 == 0:
            fat *= i
    return fat


N = int(input('Entre com um número inteiro ímpar: '))
while N % 2 == 0:
    N = int(input('Valor inválido! Entre com um número ímpar: '))

print(f'O fatorial duplo de {N} é: {fatorialduplo(N)}')
