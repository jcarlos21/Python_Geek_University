"""
Questão 03
"""


def checa_num(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


num = int(input('Entre com um número: '))

print(checa_num(num))
