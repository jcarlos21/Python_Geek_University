"""
Questão 04
"""
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior = 0
a = 0
b = 0
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Entre com o valor da posição [{l}, {c}]: '))

maior = matriz[0][0]
for l in range(0, 4):
    for c in range(0, 4):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            a = l
            b = c

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]:^3}', end='')
    print()

print(f'O maior valor da matriz é {maior} e está na posição [{a}, {b}]. ')
