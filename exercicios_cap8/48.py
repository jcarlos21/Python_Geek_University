"""
Questão 48
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


def PreencheMatrizRandom(matriz):
    for a in range(0, len(matriz)):
        for b in range(0, len(matriz[0])):
            matriz[a][b] = random.randint(0, 99)
    return matriz


def SomaAcimaDiagonalPrincipal(matriz):
    soma = 0
    for a in range(0, len(matriz)):
        for b in range(0, len(matriz[0])):
            if b > a:
                soma += matriz[a][b]
    return soma


linhas = colunas = int(input('Entre com um número inteiro para compor a matriz quadrática: '))
print()
A = PreencheMatrizRandom(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

print(f'\nA soma dos elementos acima da diagonal principal é: {SomaAcimaDiagonalPrincipal(A)}')
