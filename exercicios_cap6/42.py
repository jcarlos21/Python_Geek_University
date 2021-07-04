"""
Questão 42
"""
import math
num = 1

while num > 0:
    num = int(input('Entre com um valor (finaliza quando for menor ou igual a zero): '))
    print(f'O quadrado, o cubo e a raiz quadrada de {num} é: {num}² = {num**2}, {num}³ = {num**3} e {math.sqrt(num)}.\n')
