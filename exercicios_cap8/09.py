"""
Questão 09
"""
import math


def volume_do_cilindro(altura, raio):
    return math.pi * (raio ** 2) * altura


height = float(input('Entre com a altura do cilindro: '))
radius = float(input('Entre com o raio do cilindro: '))
print(f'O volume do cilindro é: {(volume_do_cilindro(height, radius)).__round__(2)} m³.')
