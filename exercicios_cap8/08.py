"""
Questão 08
"""
import math


def hipotenusa(a, b):
    return math.sqrt((a ** 2) + (b ** 2))


cateto_oposto = float(input('Entre com o cateto oposto: '))
cateto_adjacente = float(input('Entre com o cateto adjacente: '))
print(f'A hipotenusa é: {(hipotenusa(cateto_oposto, cateto_adjacente)).__round__(2)}')
