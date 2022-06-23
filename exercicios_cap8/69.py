"""
Questão 69
"""


def SimplificaFracao(num, den):
    if den == 0:
        return 'Denominado não pode ser zero.'
    if num < den:
        n = num
        while True or n > 0:
            if num % n == 0 and den % n == 0:
                return num / n, den / n
            n -= 1
    else:
        n = den
        while True or n > 0:
            if num % n == 0 and den % n == 0:
                return num / n, den / n
            n -= 1


def SomaFracoes(p1, q1, p2, q2):
    return ((p1*q2)+(p2*q1)) / (q1*q2)


def SubtracaoFracoes(p1, q1, p2, q2):
    return ((p1*q2)-(p2*q1)) / (q1*q2)


def ProdutoFracoes(p1, q1, p2, q2):
    return (p1*p2) / (q1*q2)


def QuocienteFracoes(p1, q1, p2, q2):
    return (p1*q2) / (p2*q1)


numerador1 = int(input('Entre com o numerador1: '))
denominador1 = int(input('Entre com o denominador1: '))
while denominador1 == 0:
    denominador1 = int(input('Denominador não pode ser zero! Digite novamente:  '))
numerador2 = int(input('Entre com o numerador2: '))
denominador2 = int(input('Entre com o denominador2: '))
while denominador2 == 0:
    denominador2 = int(input('Denominador não pode ser zero! Digite novamente:  '))

num1, den1 = SimplificaFracao(numerador1, denominador1)
num2, den2 = SimplificaFracao(numerador2, denominador2)

print(f'A soma das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a: '
      f'{SomaFracoes(num1, den1, num2, den2)}')
print(f'A subtração das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a: '
      f'{SubtracaoFracoes(num1, den1, num2, den2)}')
print(f'O produto das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a: '
      f'{ProdutoFracoes(num1, den1, num2, den2)}')
print(f'O quociente das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a: '
      f'{QuocienteFracoes(num1, den1, num2, den2)}')
