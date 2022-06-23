"""
Questão 45
"""
import math
import random


def DesvioPadraoVetor(x):
    m = sum(x)/len(x)
    soma = 0
    for i in x:
        soma += (i - m)**2
    return math.sqrt((1/(len(x)-1))*soma).__round__(2)


lista = []
for a in range(0, 30):
    aux = random.randint(10, 99)
    lista.append(aux)

print(f'Vetor gerado aleatóriamente: {lista}'
      f'\nO desvio padrão do vetor é: {DesvioPadraoVetor(lista)}')
