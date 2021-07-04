"""
Questão 11
"""
N = int(input('Entre com um número inteiro: '))
for i in range(0, N+1):
    if i == 0:
        print(f'Os inteiros positivos de 0 até {N} são:'
              f'\n{i}')
    else:
        print(i)
