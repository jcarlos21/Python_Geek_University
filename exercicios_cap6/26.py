"""
Questão 26
"""
num = int(input('Entre com um número: '))
for i in range(1, num + 1):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        if i % 11 == 0:
            print(f'{i} é múltiplo de 11.')
        if i % 13 == 0:
            print(f'{i} é múltiplo de 13.')
        if i % 17 == 0:
            print(f'{i} é múltiplo de 17.')
