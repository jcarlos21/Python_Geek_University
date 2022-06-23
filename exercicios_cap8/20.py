"""
Questão 20
"""


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat = fat * i
    return fat


num = int(input('Entre com um número inteiro para cálcular o fatorial: '))
print(f'O fatorial de {num} é: {fatorial(num)}')
