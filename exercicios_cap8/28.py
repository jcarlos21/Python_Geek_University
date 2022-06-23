"""
Questão 28
"""
import math


def GradoToRadiano(x):
    return x * (math.pi/180)


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat = fat * i
    return fat


def CossenoTaylor(x):
    soma = 0
    for i in range(0, 100):
        soma += ((-1)**i / (fatorial(2*i))) * (x ** (2*i))
    return soma


num = int(input('Entre com um valor em graus: '))
print(f'A série cosseno de Taylor para o grau digitado é: {CossenoTaylor(GradoToRadiano(num))}')
