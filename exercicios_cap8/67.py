"""
Questão 67
"""


def rotina(tam):
    n = 0
    while n < tam:
        string = input('Digite um caractere ou enter: ')
        if not string:
            break
        n += 1


rotina(tam=3)
