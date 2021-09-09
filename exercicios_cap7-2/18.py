"""
Questão 18
"""
import random
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        matriz[i][j] = random.randint(0, 100)

print('\nA matriz gerada é:\n')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end='')
    print()

vetor = [0, 0, 0]
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        vetor[i] += matriz[j][i]

print(f'\nO vetor da soma das colunas é: {vetor}')
