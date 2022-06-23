"""
Questão 04
"""


def checa_quadrado(x):
    i = 1
    while True:
        if x == i ** 2:
            return i  # O return finaliza a execução da função
        else:
            if i == x:
                return 0
        i += 1


num = int(input('Entre com um número inteiro: '))
if checa_quadrado(num) == 0:
    print(f'O número {num} não é um quadrado perfeito.')
else:
    print(f'O número {num} é um quadrado perfeito e é resultado da operação {checa_quadrado(num)}² = {num}.')
