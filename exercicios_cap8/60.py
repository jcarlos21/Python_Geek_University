"""
Questão 60
"""


def RetornaPosicaoSubstring(lista):
    if len(lista.split()) > 1:
        return lista.split()[0]
    else:
        return -1


dado = input('Entre com uma palavra ou frase: ')
print(f'Resultado para retorno da substring: {RetornaPosicaoSubstring(dado)}')
