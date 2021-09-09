"""
Questão 20
"""
import random
matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
num = 0.0
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        num = random.uniform(0, 99)
        matriz[i][j] = num.__round__(2)

print('Matriz original:\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()

soma = 0
cont2 = 0
cont4 = 0
soma_2_coluna = 0
soma_4_coluna = 0

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        if j % 2 == 0:  # soma de todos os elementos das colunas ímpares (lembrando que o índice zero é primeiro
            # elemento)
            soma += matriz[i][j]
        if j == 1:
            soma_2_coluna += matriz[i][j]
            cont2 += 1
        elif j == 3:
            soma_4_coluna += matriz[i][j]
            cont4 += 1
        if j == 5:
            matriz[i][j] = (matriz[i][0] + matriz[i][1]).__round__(2)

print(f'\nA soma de todos elementos das colunas ímpares é: {soma.__round__(2)}'
      f'\nA média aritmética da segunda e quarta coluna é: {(soma_2_coluna / cont2).__round__(2)}; '
      f'{(soma_4_coluna / cont4).__round__(2)}')

print()
print('Matriz modificada:\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        print(f'[{matriz[i][j]:^7}]', end=' ')
    print()
