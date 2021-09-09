"""
Questão 11
"""
import random
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        matriz[i][j] = random.randint(0, 10)

soma = 0
j = 0
for i in range(len(matriz)-1, -1, -1):
    soma += matriz[i][j]
    j += 1

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        print(f'{matriz[i][j]:^3}', end='')
    print()
print(f'\nA soma da diagonal secundária da matriz é: {soma}')
