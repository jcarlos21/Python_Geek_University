"""
Questão 29
"""
n = int(input('Entre com o valor: '))


def fatorial(x):
    fat = 1
    if x == 0:
        return 1
    else:
        for g in range(1, x + 1):
            fat = fat * g
    return fat


S = 0
for i in range(1, n + 1):
    S = S + (i / fatorial(2*i))
print(f'A série tende a {S}.')
