"""
Questão 43
"""
import random


def Preenche_Vetor(x, tamanho):
    for a in range(0, tamanho):
        x.append(random.randint(0, 100))
    return x


tam = int(input('Entre com o tamanho da lista: '))
lista = list()
lista = Preenche_Vetor(lista, tam)
print(f'O maior valor da lista é {lista}.')
