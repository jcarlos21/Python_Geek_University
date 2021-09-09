"""
Questão 24
"""
import random


def gera_matriz(linha, coluna):  # função que gera um matriz nxm
    matriz = []
    laco = 0
    while laco < linha:  # geração de linhas da matriz
        matriz.append([])
        laco += 1
    for b in range(0, linha):  # geração de colunas e dos elementos de cada linha
        for c in range(0, coluna):
            matriz[b].append(0)
    return matriz


print('Entre com o número de linhas e colunas para compor a matriz quadrática:')
linhas = colunas = 20
# int(input('N° de linhas é igual ao nº de colunas (maior ou igual a 4): '))

A = gera_matriz(linhas, colunas)

for i in range(0, len(A)):  # preenchimento da matriz com números aleatórios
    for j in range(0, len(A[i])):
        A[i][j] = random.randint(0, 99)

print('\nA matrizes gerada é: ')
print()

for i in range(0, linhas):  # impressão da matriz
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

maior = 0
maior_linha = -1
maior_coluna = -1
maior_diagonal_principal = -1
maior_diagonal_secundaria = -1

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0

b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0

d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0

for i in range(0, linhas):
    for j in range(0, colunas):
        if j < (colunas - 3):
            if A[i][j] * A[i][j + 1] * A[i][j + 2] * A[i][j + 3] > maior_linha:  # conferência em linha por linha
                maior_linha = A[i][j] * A[i][j + 1] * A[i][j + 2] * A[i][j + 3]
                a1 = i
                a2 = j
                a3 = i
                a4 = j + 1
                a5 = i
                a6 = j + 2
                a7 = i
                a8 = j + 3

            if A[j][i] * A[j + 1][i] * A[j + 2][i] * A[j + 3][i] > maior_coluna:  # conferencia coluna por coluna
                maior_coluna = A[j][i] * A[j + 1][i] * A[j + 2][i] * A[j + 3][i]
                b1 = j
                b2 = i
                b3 = j + 1
                b4 = i
                b5 = j + 2
                b6 = i
                b7 = j + 3
                b8 = i

for a in range(0, linhas):  # diagonais principais e secundárias
    for i in range(0, linhas):
        for j in range(0, colunas):
            if (i < linhas - 3) and (j < colunas - 3):
                if A[i][j] * A[i + 1][j + 1] * A[i + 2][j + 2] * A[i + 3][j + 3] > maior_diagonal_principal:
                    maior_diagonal_principal = A[i][j] * A[i + 1][j + 1] * A[i + 2][j + 2] * A[i + 3][j + 3]
                    c1 = i
                    c2 = j
                    c3 = i + 1
                    c4 = j + 1
                    c5 = i + 2
                    c6 = j + 2
                    c7 = i + 3
                    c8 = j + 3
    for i in range(linhas - 1, 2, -1):
        for j in range(0, colunas-3):
            if A[i][j] * A[i - 1][j + 1] * A[i - 2][j + 2] * A[i - 3][j + 3] > maior_diagonal_secundaria:
                maior_diagonal_secundaria = A[i][j] * A[i - 1][j + 1] * A[i - 2][j + 2] * A[i - 3][j + 3]
                d1 = i
                d2 = j
                d3 = i - 1
                d4 = j + 1
                d5 = i - 2
                d6 = j + 2
                d7 = i - 3
                d8 = j + 3

if maior_linha > maior_coluna and maior_linha > maior_diagonal_principal and maior_linha > maior_diagonal_secundaria:
    print(f'\nA multiplicação foi em linha e é igual a: {maior_linha}'
          f'\nOs números multiplicados foram: {A[a1][a2]}, {A[a3][a4]}, {A[a5][a6]}, {A[a7][a8]}'
          f'\nOs índice foram: [{a1}, {a2}], [{a3}, {a4}], [{a5}, {a6}], [{a7}, {a8}].')
elif maior_coluna > maior_linha and maior_coluna > maior_diagonal_principal and maior_coluna > maior_diagonal_secundaria:
    print(f'\nA multiplicação foi em coluna e é igual a: {maior_coluna}'
          f'\nOs números multiplicados foram: {A[b1][b2]}, {A[b3][b4]}, {A[b5][b6]}, {A[b7][b8]}'
          f'\nOs índice foram: [{b1}, {b2}], [{b3}, {b4}], [{b5}, {b6}], [{b7}, {b8}].')
elif maior_diagonal_principal > maior_diagonal_secundaria and maior_diagonal_principal > maior_linha and maior_diagonal_principal > maior_coluna:
    print(f'\nA multiplicação foi em diagonais principais e é igual a: {maior_diagonal_principal}'
          f'\nOs números multiplicados foram: {A[c1][c2]}, {A[c3][c4]}, {A[c5][c6]}, {A[c7][c8]}'
          f'\nOs índice foram: [{c1}, {c2}], [{c3}, {c4}], [{c5}, {c6}], [{c7}, {c8}].')
else:
    print(f'\nA multiplicação foi em diagonais secundárias e é igual a: {maior_diagonal_secundaria}'
          f'\nOs números multiplicados foram: {A[d1][d2]}, {A[d3][d4]}, {A[d5][d6]}, {A[d7][d8]}'
          f'\nOs índice foram: [{d1}, {d2}], [{d3}, {d4}], [{d5}, {d6}], [{d7}, {d8}].')

print(f'\nLinha: {maior_linha}'
      f'\nÍndices da linda: [{a1}, {a2}], [{a3}, {a4}], [{a5}, {a6}], [{a7}, {a8}]'
      f'\nColuna: {maior_coluna}'
      f'\nÍndices da coluna: [{b1}, {b2}], [{b3}, {b4}], [{b5}, {b6}], [{b7}, {b8}]'
      f'\nDiagonais principais: {maior_diagonal_principal}'
      f'\nÍndices da diagonal: [{c1}, {c2}], [{c3}, {c4}], [{c5}, {c6}], [{c7}, {c8}]'
      f'\nDiagonais secundárias: {maior_diagonal_secundaria}'
      f'\nÍndices da diagonal: [{d1}, {d2}], [{d3}, {d4}], [{d5}, {d6}], [{d7}, {d8}].')
