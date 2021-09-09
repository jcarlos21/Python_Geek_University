"""
Questão 06
"""

matriz1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz1[l][c] = int(input(f'Entre com o valor da posição [{l}, {c}] da matriz 1: '))

for l in range(0, 4):
    for c in range(0, 4):
        matriz2[l][c] = int(input(f'Entre com o valor da posição [{l}, {c}] da matriz 2: '))

for l in range(0, 4):
    for c in range(0, 4):
        if matriz1[l][c] > matriz2[l][c]:
            matriz3[l][c] = matriz1[l][c]
        else:
            matriz3[l][c] = matriz2[l][c]

for i in range(0, 4):
    for j in range(0, 4):
        print(f'{matriz3[i][j]:^3}', end='')
    print()
