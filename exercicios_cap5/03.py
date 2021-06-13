"""
Questão 03
"""
import math
num = float(input('Digite um número real: '))
if num >= 0:
    print(f'A raiz quadrada do número digitado é: {(math.sqrt(num)).__round__(2)}')
else:
    print(f'O quadrado do número digitado é: {(num ** 2).__round__(2)}')
