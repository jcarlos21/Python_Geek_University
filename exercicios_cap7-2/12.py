"""
Questão 12
"""
import random
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        matriz[i][j] = random.randint(0, 10)

print('A matriz original é:\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        print(f'{matriz[i][j]:^3}', end='')
    print()

print('\nA transposta da matriz é:\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        print(f'{matriz[j][i]:^3}', end='')
    print()
