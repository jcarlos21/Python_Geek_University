"""
Questão 22
"""
import random
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

num = 0.0
for i in range(0, len(A)):
    for j in range(0, len(A)):
        num = random.randint(0, 9)
        A[i][j] = num.__round__(2)

print('A matrizes gerada é: ')
print()
for i in range(0, len(A)):
    for j in range(0, len(A)):
        print(f'{A[i][j]:^5}', end='')
    print()

print()
print('O produto das duas matrizes é: ')
print()

soma = 0
for i in range(0, len(A)):
    for j in range(0, len(A)):
        for g in range(0, len(A)):
            soma += A[i][g] * A[g][j]
        C[i][j] = soma
        soma = 0

for i in range(0, len(A)):
    for j in range(0, len(A)):
        print(f'{C[i][j]:^5}', end='')
    print()
