"""
Questão 21
"""
import random

A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]
num = 0

for i in range(0, len(A)):
    for j in range(0, len(B[0])):
        num = random.uniform(0, 100)
        A[i][j] = num.__round__(2)
        num = random.uniform(0, 100)
        B[i][j] = num.__round__(2)

opcao = input(f'Entre com uma das opções abaixo:\n'
              f'\n1 - somar as duas matrizes'
              f'\n2 - subtrair as duas matrizes'
              f'\n3 - adicionar um constante às duas matrizes'
              f'\n4 - imprimir as matrizes geradas aleatóriamente'
              f'\nOpção: ')
print()
somaABsub = [[0, 0], [0, 0]]
constante = 0.0
if opcao == '1':
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            somaABsub[i][j] = (A[i][j] + B[i][j]).__round__(2)
            print(f'{somaABsub[i][j]:^4}', end='')
        print()
elif opcao == '2':
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            somaABsub[i][j] = (B[i][j] - A[i][j]).__round__(2)
            print(f'{somaABsub[i][j]:^4}', end='')
        print()
elif opcao == '3':
    constante = float(input('Entre com o valor da constante: '))
    for i in range(0, len(A)):
        for g in range(0, len(B)):
            A[i][g] = A[i][g] + constante
            B[i][g] = B[i][g] + constante

    print('Matrizes modificadas:\n')
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            print(f'[{A[i][j]:^5}]', end=' ')
        print()

    print()
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            print(f'[{B[i][j]:^5}]', end=' ')
        print()
else:
    print('\nMatrizes originais:\n')
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            print(f'[{A[i][j]:^5}]', end=' ')
        print()

    print()
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            print(f'[{B[i][j]:^5}]', end=' ')
        print()
