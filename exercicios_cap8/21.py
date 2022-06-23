"""
Questão 21
"""


def EhPrimo(x):
    cont = 0
    for i in range(1, x+1):
        if x % i == 0:
            cont += 1
    if x == 1:
        return True
    elif cont == 2:
        return True
    return False


def conta(x):
    cont = 0
    for i in range(1, x):
        if EhPrimo(i):
            cont += 1
    return cont


num = int(input('Entre com o número inteiro: '))
print(f'Há {conta(num)} números primos abaixo de {num}.')

