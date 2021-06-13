"""
Questão 20
"""
Lado1 = input('Entre com o primeiro lado do triângulo: ')
Lado2 = input('Entre com o segundo lado do triângulo: ')
Lado3 = input('Entre com o terceiro lado do triângulo: ')

while Lado1.isalpha() or Lado2.isalpha() or Lado3.isalpha():
    print('O valor digitado não corresponde ao esperado. Por favor digite o esperado.')
    Lado1 = input('Lado 1: ')
    Lado2 = input('Lado 2: ')
    Lado3 = input('Lado 3: ')

a = float(Lado1)
b = float(Lado2)
c = float(Lado3)

# É triângulo?
if (a < b + c) and (b < a + c) and (c < a + b):
    print('\nOs lados digitados são de um triângulo!')
    if a == b == c:
        print('\nO triângulo digitado é equilátero.')
    elif (a == b != c) or (b == c != a) or (a == c != b):
        print('\nO triângulo digitado é isósceles.')
    else:
        if a != b != c:
            print('\nO triângulo é escaleno.')
else:
    print('\nNão é um trinagulo.')
