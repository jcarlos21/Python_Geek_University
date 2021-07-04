"""
Questão 12
"""
N = int(input('Entre com um número inteiro: '))
for i in range(N, -1, -1):  # é preciso pôr o passo sempre
    if i == N:
        print(f'Os inteiros positivos de {N} até 0 são:'
              f'\n{i}')
    else:
        print(i)
