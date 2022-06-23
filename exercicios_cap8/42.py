"""
Questão 42
"""


def mediavetor(x):
    return sum(x)/len(x)


tam = int(input('Entre com o tamanho da lista: '))
lista = []
aux = 0.0
for i in range(0, tam):
    aux = float(input(f'Entre com o valor da {i+1}ª posição: '))
    lista.append(aux)

print(f'O maior valor da lista é {mediavetor(lista)}.')

