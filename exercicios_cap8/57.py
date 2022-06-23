"""
Questão 56
"""
import random


def GeraMatriz(linha, coluna):
    matriz = []
    laco = 0
    while laco < linha:
        matriz.append([])
        laco += 1
    for a in range(0, linha):
        for b in range(0, coluna):
            matriz[a].append([])
    return matriz


def PreencheMatriz(x):
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            x[a][b] = random.randint(0, 99)
    return x


def SomaColuna(x, coluna):
    soma = 0
    for a in range(0, len(x)):
        soma += x[a][coluna]  # O que fica alterando a cada iteração é a coluna
    return soma


linhas = int(input('Entre com o número de linhas da matriz: '))
colunas = int(input('Entre com o número de coluna da matriz: '))
A = PreencheMatriz(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

N = int(input('\nEntre com a coluna que deseja ter os elementos somados: '))
print(f'A soma dos elementos da coluna {N-1} é: {SomaColuna(A, N-1)}')
