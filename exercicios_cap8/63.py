"""
Questão 63
"""


def EhIgual(s1, s2):
    cont = 0
    if len(s1) < len(s2):
        for a in range(0, len(s1)):
            if s1[a] == s2[a]:
                cont += 1
        if cont == len(s2):
            return True
        else:
            return False
    else:
        for a in range(0, len(s2)):
            if s1[a] == s2[a]:
                cont += 1
        if cont == len(s1):
            return True
        else:
            return False


string01 = input('Entre com palavra ou frase: ')
string02 = input('Entre com outra palavra ou outra frase para comparar: ')
if EhIgual(string01, string02):
    print('Os textos ou palavras são iguais.')
else:
    print('Os textos ou palavras não são iguais.')
