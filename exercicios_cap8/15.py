"""
Questão 15
"""


def e_triangulo(a, b, c):
    if a < b + c:
        return True
    elif b < a + c:
        return True
    elif c < a + b:
        return True
    else:
        return False


def tipo_triangulo(a, b, c):
    if a == b == c:
        return 'O lados informados formam um triângulo equiátero.'
    elif a == b != c:
        return 'O lados informados formam um triângulo isóceles.'
    elif a == c != b:
        return 'O lados informados formam um triângulo isóceles.'
    elif b == c != a:
        return 'O lados informados formam um triângulo isóceles.'
    else:
        return 'O lados informados formam um triângulo escaleno.'


lado_a = int(input('Entre com o primeiro lado triângulo: '))
lado_b = int(input('Entre com o segundo lado triângulo: '))
lado_c = int(input('Entre com o terceiro lado triângulo: '))

if not e_triangulo(lado_a, lado_b, lado_c):
    print('Os valores informados não correspondem a um triângulo!')
else:
    print(f'\n{tipo_triangulo(lado_a, lado_b, lado_c)}')
