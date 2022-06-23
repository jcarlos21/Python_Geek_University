"""
Questão 61
"""


def ComparaStrings(string1, string2):
    cont = 0
    for a in range(0, len(string1)):
        if string2.count(string1[a]) > 0:
            cont += 1
    if cont == len(string1):
        return True
    return False


texto1 = input('Entre com uma palavra ou uma frase: ')
texto2 = input('Entre com uma palavra ou uma frase para comparar: ')
if ComparaStrings(texto1, texto2):
    print('\nO texto 1 é anagrama do texto 2!')
else:
    print('\nO texto 1 não é anagrama do texto 2!')
