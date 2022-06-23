"""
Questão 30
"""


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat = fat * i
    return fat


def CossenoHTaylor(x):
    soma = 0.0
    for i in range(0, 500):
        soma += (x ** (2*i)) / fatorial(2*i)
    return soma


num = int(input('Entre com um valor em graus: '))
print(f'A série cosseno  hiperbólico de Taylor para o grau digitado é: {CossenoHTaylor(num)}')
