"""
Questão 14
"""
import random

cartela = [[100, 100, 100, 100, 100], [100, 100, 100, 100, 100], [100, 100, 100, 100, 100], [100, 100, 100, 100, 100],
           [100, 100, 100, 100, 100]]
# sum(x.count(1) for x in cartela) contagem em lista de listas, ou seja, matrizes. É uma outra possibilidade!


def conferencia(matriz, dado):
    soma = 0
    for value in matriz:
        soma += value.count(dado)
    if soma > 0:
        return True
    else:
        return False


valor = 0
for i in range(0, len(cartela)):
    for j in range(0, len(cartela)):
        valor = random.randint(0, 99)
        while conferencia(cartela, valor):
            valor = random.randint(0, 99)
        cartela[i][j] = valor

print('A cartela é:\n')
for i in range(0, len(cartela)):
    for j in range(0, len(cartela)):
        print(f'{cartela[i][j]:^3}', end='')
    print()
