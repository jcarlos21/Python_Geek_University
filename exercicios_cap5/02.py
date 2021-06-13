"""
Questão 02
"""
import math

num = float(input('Digite um número: '))
if num >= 0:
    print(f'A raiz quadrada do número digitado é: {(math.sqrt(num)).__round__(2)}')
else:
    while num < 0:
        num = float(input('O número digitado é inválido. Por favor entre com um número maior que zero: '))
        if num >= 0:
            print(f'A raiz quadrada do número digitado é: {(math.sqrt(num)).__round__(2)}')
