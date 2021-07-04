"""
Questão 13
"""
N = int(input('Entre com um número inteiro: '))
for i in range(0, N+1):
    if i == 0 and i % 2 == 0:
        print(f'Os inteiros positivos pares de 0 até {N} são:'
              f'\n{i}', end=', ')
    elif i % 2 == 0:
        if N - 1 == i:
            print(i, end='.')
        elif N == i:
            print(i, end='.')
        else:
            print(i, end=', ')
