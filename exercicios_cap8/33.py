"""
Questão 33
"""


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat


def somaalgarismoNfatorial(x):
    num = fatorial(x)
    soma = 0
    while num != 0:
        soma += num % 10
        num //= 10
    return soma


numero = int(input('Entre com um número inteiro: '))
print(f'{numero}! é: {fatorial(numero)}')
print(f'A soma dos algarismos de {numero}! é: {somaalgarismoNfatorial(numero)}')
