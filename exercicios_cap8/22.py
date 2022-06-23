"""
Qustão 22
"""


def imprimeexclamacao(x):
    return '!' * x


num = int(input('Entre com um valor inteiro: '))

for i in range(1, num+1):
    print(imprimeexclamacao(i))
