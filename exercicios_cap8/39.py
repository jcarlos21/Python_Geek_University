"""
Questão 39
"""


def Troque(A, B):
    aux = A
    A = B
    B = aux
    return [A, B]


numA = float(input('Entre com um valor real: '))
numB = float(input('Entre com outro valor real: '))
print(f'O valores {numA} e {numB} trocados são: {Troque(numA, numB)} ')
