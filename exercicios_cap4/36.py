"""
Questão 36
"""
import math
print('Cálculo do volume de um cilindro circular')
altura = float(input('Entre com a altura do cilindro: '))
raio = float(input('Entre com o raio do cilindro: '))
print(f'O volume do cilindro é: {(math.pi * (raio ** 2) * altura).__round__(2)} m3')
