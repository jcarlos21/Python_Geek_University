"""
Questão 08
"""
import random
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = random.randint(0, 10)
        if not i == j and j > i:
            soma += matriz[i][j]

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^3}', end='')
    print()
print(f'\nA soma da parte superior da matriz é: {soma}')
