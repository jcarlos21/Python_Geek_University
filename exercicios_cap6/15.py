"""
Questão 15
"""
N = int(input('Entre com um número inteiro ímpar: '))
for i in range(0, N+1):
    if i % 2 == 1 and i == 1:
        print(f'Os números ímpares de {i} até {N} são:'
              f'\n{i}')
    elif i % 2 == 1:
        print(i)
