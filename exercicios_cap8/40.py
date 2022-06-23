"""
Questão 40
"""


def ContaPar(x):
    cont = 0
    for i in x:
        if i % 2 == 0:
            cont += 1
    return cont


tam = int(input('Entre com o tamanho da lista: '))
lista = []
aux = 0
for i in range(0, tam):
    aux = int(input(f'Entre com o valor da {i+1}ª posição: '))
    lista.append(aux)

print(f'A lista digitada possui {ContaPar(lista)} números pares.')
