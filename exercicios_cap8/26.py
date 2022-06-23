"""
Questão 26
"""


def SomaDe1aN(N):
    soma = 0
    for i in range(0, N+1):
        soma += i
    return soma


num = int(input('Entre com um número inteiro: '))
print(f'Soma dos números de {1} a {num}: {SomaDe1aN(num)}')

