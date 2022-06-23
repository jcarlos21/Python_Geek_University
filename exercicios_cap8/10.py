"""
Questão 10
"""


def maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


numero1 = float(input('Entre com um número: '))
numero2 = float(input('Entre com outro número: '))
print(f'O maior dos números digitados é: {maior(numero1, numero2)}')
