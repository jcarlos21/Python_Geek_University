"""
Questão 13
"""
import random
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        matriz[i][j] = random.randint(1, 20)

print('A matriz original é:\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        print(f'{matriz[i][j]:^3}', end='')
    print()

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        if not i == j and i < j:
            matriz[i][j] = 0

print('\nA matriz triangular inferior é:\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        print(f'{matriz[i][j]:^3}', end='')
    print()
