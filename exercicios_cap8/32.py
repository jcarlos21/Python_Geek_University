"""
Questão 32
"""


def recebenum(x):
    return x


def simplifica(numerador, denominador):
    a = denominador
    while denominador != 0:
        if numerador % a == 0 and denominador % a == 0:
            return numerador/a, denominador/a
        a -= 1
    return numerador, denominador


num, deno = simplifica(36, 60)
print(f'A fração original é {36}/{60}. A nova fração simplicada é: {num}/{deno}')
