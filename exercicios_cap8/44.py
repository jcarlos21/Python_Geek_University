"""
Questão 44
"""
import random


def separavetor(x):
    a = []
    b = []
    for i in range(0, len(x)):
        if x[i] % 2 == 0:
            a.append(x[i])
        else:
            b.append(x[i])
    return a, b


lista = []
for i in range(0, 30):
    aux = random.randint(25, 100)
    lista.append(aux)

vetorpar, vetorimpar = separavetor(lista)
print(f'Vetor par: {vetorpar}'
      f'\nVetor ímpar: {vetorimpar}')
