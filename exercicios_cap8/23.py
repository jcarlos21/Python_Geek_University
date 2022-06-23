"""
Questão 23
"""


def imprimeasterisco(n):
    g = 1
    for i in range(0, (2 * n - 1)):
        print('*' * g)
        if (i + 1) >= n:
            g -= 1
        else:
            g += 1


imprimeasterisco(4)
