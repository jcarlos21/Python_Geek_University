"""
Questão 05
"""
import math


def volume_da_esfera(raio):
    return (4 / 3) * math.pi * (raio ** 3)


Raio = input('Entre com o valor do raio: ')
print(f'O volume para um raio de {Raio} é {(volume_da_esfera(float(Raio))).__round__(2)} m³.')
