"""
Questão 41
"""


def maior(x):
    return max(x)


def big(x):
    biggest = x[0]
    for a in range(0, len(x)):
        if x[a] > biggest:
            biggest = x[a]
    return biggest


tam = int(input('Entre com o tamanho da lista: '))
lista = []
aux = 0
for i in range(0, tam):
    aux = int(input(f'Entre com o valor da {i+1}ª posição: '))
    lista.append(aux)

print(f'O maior valor da lista é {big(lista)}.')
