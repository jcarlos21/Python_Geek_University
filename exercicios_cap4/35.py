"""
Questão 35
"""
import math

print('Cálculo da hipotenusa')
a = float(input('Entre com o primeiro cateto do triângulo retângulo: '))
b = float(input('Entre com o segundo cateto do triângulo retângulo: '))
print(f'A hipotenusa é: {(math.sqrt((a ** 2) + (b ** 2))).__round__(2)}')
