"""
Questão 25
"""
import math
print(f'Raízes da equação 2° grau na forma ax² + bx + c = 0 ')
a = float(input('Entre com um valor de "a" diferente de zero: '))
while a == 0:
    a = float(input('Valor inválido! Entre com um valor de "a" diferente de zero:'))

b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = float((b ** 2) - 4 * a * c)

print()
if delta < 0:
    print('Não existe raiz real.')
elif delta == 0:
    print(f'Raiz única: {(-b) / (2 * a)}')
else:
    print(f'Há duas raízes!'
          f'\nRaiz 1: {((-b) + math.sqrt(delta)) / (2 * a)}'
          f'\nRaiz 2: {((-b) - math.sqrt(delta)) / (2 * a)}')