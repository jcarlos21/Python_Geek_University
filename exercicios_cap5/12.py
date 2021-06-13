"""
Questão 12
"""
import math
num = float(input('Entre com um número: '))
if num == 0:
    print('O logarítmo de zero é indefinido.')
elif num > 0:
    print(f'O logarítmo de {num} é igual a {(math.log(num, 10)).__round__(2)}')
else:
    print('Número inválido.')
