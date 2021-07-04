"""
Questão 16
"""
N = int(input('Entre com um número inteiro ímpar: '))
for i in range(N, -1, -1):
    if i % 2 == 1 and i == N:
        print(f'Os números ímpares de {i} até {N} são:'
              f'\n{i}')
    else:
        print(i)
