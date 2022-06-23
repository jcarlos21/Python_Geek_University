"""
Questão 47
"""
import random


def GeraMatriz(linha, coluna):
    matriz = []
    laco = 0
    while laco < linha:
        matriz.append([])  # Aqui será criado um vetor de listas [] vazias.
        laco += 1
    for a in range(0, linha):
        for b in range(0, coluna):
            matriz[a].append([])  # Adicionando colunas (em cada linha 'a' será adicionada [] vazias).
    return matriz


def retornamaiorque10(matriz, num):
    cont = 0
    for c in range(0, len(matriz)):
        for d in range(0, len(matriz[c])):
            if matriz[c][d] > num:
                cont += 1
    return cont


linhas = colunas = int(input('Entre com o número de linhas e colunas para compor a matriz quadrática: '))
numero = int(input('Entre com o número que deseja consultar na matriz: '))
print()
A = GeraMatriz(linhas, colunas)  # Geração da matriz

for i in range(0, linhas):  # preenchimento da matriz com números aleatórios
    for j in range(0, colunas):
        A[i][j] = random.randint(0, 99)

for i in range(0, linhas):  # Impressão de matriz
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

print(f'\nExistem {retornamaiorque10(A, num = numero)} número maiores que {numero} na matriz.')

