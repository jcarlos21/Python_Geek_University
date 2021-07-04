"""
Questão 14
"""
N = int(input('Entre com um número inteiro: '))
for i in range(N, -1, -1):
    if i == N and i % 2 == 0:
        print(f'Os inteiros positivos pares de 0 até {N} são:'
              f'\n{i}', end=', ')
    elif i % 2 == 0:
        if 0 == i:
            print(i, end='.')
        else:
            print(i, end=', ')
