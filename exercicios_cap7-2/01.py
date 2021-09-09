"""
Questão 01
"""
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
cont = 0
for linha in range(0, 4):
    for coluna in range(0, 4):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] > 10:
            cont += 1
print()
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]:^5}', end='')
    print()
    if l == 3:
        print(f'\nA matriz possui {cont} números acima de {10}.')
