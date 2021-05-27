"""
Questão 47
"""
"""num = input('Entre com um número inteiro de 4 dígitos: ')
print(f'Dígito 1: {num[0]}')
print(f'Dígito 1: {num[1]}')
print(f'Dígito 1: {num[2]}')
print(f'Dígito 1: {num[3]}')
"""

num = input('Entre com um número inteiro de 4 dígitos: ')
while len(num) != 4:
    num = input('Entre com um número inteiro de apenas 4 dígitos: ')

i = 0
while i < len(num):
    print(f'Dígito {i}: {num[i]}')
    i += 1
