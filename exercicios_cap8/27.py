"""
Questão 27
"""
import math


def GradoToRadiano(x):
    return x * (math.pi/180)


def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat = fat * i
    return fat


def SenoTaylor(x):
    soma = 0
    for i in range(0, 6):
        soma += ((-1)**i / (fatorial(2*i + 1))) * (x ** (2*i+1))
    return soma


num = int(input('Entre com um valor em graus: '))
print(f'A série seno de Taylor para o grau digitado é: {SenoTaylor(GradoToRadiano(num))}')
