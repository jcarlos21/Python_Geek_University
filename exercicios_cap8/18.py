"""
Questão 18
"""


def exponenciacao(x, z):
    return x ** z


base = int(input('Entre com o valor da base: '))
expoente = int(input('Entre com o valor do expoente: '))

print(f'\nO resultado é: {exponenciacao(base, expoente)}')
