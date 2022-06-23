"""
Questão 70
"""


def Reduz(a, b):
    return a / b


def neg(racional):
    return - racional


def Soma(x, y):
    return x + y


def Mult(x, y):
    return x * y


def Div(x, y):
    return x / y


print('Entre com dois números racionais para fazer operações:')
p1 = int(input('Entre com um número inteiro: '))
q1 = int(input('Entre com um outro número inteiro: '))
p2 = int(input('Entre com um segundo número inteiro: '))
q2 = int(input('Entre com um outro segundo número inteiro: '))

racional1 = Reduz(p1, q1)
racional2 = Reduz(p2, q2)

print(f'Os negativos dos números racionais {racional1} e {racional2} são {neg(racional1)} e {neg(racional2)} respectivamente.')
print(f'A soma dos racionais {racional1} e {racional2} é igual a {Soma(racional1, racional2)}')
print(f'O produto dos racionais {racional1} e {racional2} é igual a {Mult(racional1, racional2)}')
print(f'O quociente dos racionais {racional1} e {racional2} é igual a {(Div(racional1, racional2)).__round__(2)}')
