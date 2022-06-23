"""
Questão 36
"""
"""
lista = ['Carlos', 'Ana', 'José', 'Paula']

for i, valor in enumerate(lista):
    print(i, valor)
"""


def fatorial(x):
    fat = 1
    for i in range(1, x + 1):
        fat *= i
    return fat


def superfatorial(x):
    sf = 1
    for i in range(1, x + 1):
        sf *= fatorial(i)
    return sf


num = int(input('Entre com um número inteiro: '))
print(f'O superfatorial de {num} é: {superfatorial(num)}')
