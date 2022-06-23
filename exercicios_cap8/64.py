"""
Questão 64
"""


def ConcatenaStrings(str1, str2):
    return str1 + ' ' + str2


string01 = input('Entre com palavra ou frase: ')
string02 = input('Entre com outra palavra ou outra frase para comparar: ')
print(f'Os textos ou palavras inseridos concatenados ficam: {ConcatenaStrings(string01, string02)}')

