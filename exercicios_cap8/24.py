"""
Questão 25
"""


def arvore_de_natal(x):
    g = x - 1
    for i in range(1, x + 1):
        print(' ' * g, '*' * (2 * i - 1))
        g -= 1


arvore_de_natal(6)
