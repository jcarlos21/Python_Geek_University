"""
Questão 62
"""


def ComprimentoString(x):
    cont = 0
    for a in range(0, len(x)):
        cont += 1
    return cont


print(f'{ComprimentoString("Eu amo Pyhton!")}')
print(len('Eu amo Python!'))

