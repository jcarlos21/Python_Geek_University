"""
Questão 29
"""


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat = fat * i
    return fat


def SenoHTaylor(x):
    soma = 0.0
    for i in range(0, 500):
        soma += (x ** (2*i + 1)) / fatorial(2*i + 1)
    return soma


num = int(input('Entre com um valor em graus: '))
print(f'A série seno  hiperbólico de Taylor para o grau digitado é: {SenoHTaylor(num)}')
