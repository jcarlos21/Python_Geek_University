"""
Questão 65
"""


def ConcatenaStrings(str1, str2, n):
    return str1 + str2[:n]


string01 = input('Entre com palavra ou frase: ')
string02 = input('Entre com outra palavra ou outra frase para comparar: ')
N = int(input('Entre com um número inteiro: '))
print(f'Os textos ou palavras inseridos concatenados ficam: {ConcatenaStrings(string01, string02, N)}')
