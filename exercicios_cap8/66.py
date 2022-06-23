"""
Questão 66
"""


def Maiusculo(String):
    return String.title()


string = input('Entre com um caractere: ')
print(f'O caractere {string} transformado em maiúsculo é: {Maiusculo(string)}')
