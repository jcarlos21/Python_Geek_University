"""
Questão 03
"""
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = l * c

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]:^3}', end='')
    print()
