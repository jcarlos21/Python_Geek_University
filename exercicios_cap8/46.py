"""
Questão 46
"""
import random


def ImpressaoVetor(x):
    print(f'O vetor é: {x}')


def ImpressaoVetorInversa(x):
    print(f'O vetor na ordem inversa é: {x[::-1]}')


def MediaAritmeticaVetor(x):
    return sum(x)/len(x)


lista = []
for a in range(0, 10):
    aux = random.randint(10, 99)
    lista.append(aux)

ImpressaoVetor(lista)
ImpressaoVetorInversa(lista)
print(f'A média aritmética do vetor é: {(MediaAritmeticaVetor(lista)).__round__(2)}')
