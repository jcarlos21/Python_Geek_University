"""
Questão 12
"""


def soma_de_algarismos(num):
    soma = 0
    while num != 0:
        soma += num % 10
        num = num // 10
    return soma


numero = int(input('Entre com um número inteiro maior que zero: '))
if numero <= 0:
    print('Número inválido.')
else:
    print(f'A somas dos algorismos do número {numero} é: {soma_de_algarismos(numero)}')
