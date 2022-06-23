"""
Questão 13
"""


def operacao(num1, num2, simbolo):
    if simbolo == '+':
        return num1 + num1
    elif simbolo == '-':
        return num1 - num2
    elif simbolo == '/':
        return num1 / num2
    elif simbolo == '*':
        return num1 * num2


numero1 = float(input('Entre com um número: '))
numero2 = float(input('Entre com outro número: '))
symbol = input('Entre com um símbolo: ')
print(f'O resultado da operação é: {(operacao(numero1, numero2, symbol))}')
