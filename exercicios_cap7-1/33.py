"""
Questão 33
"""
valor = 0
vetor = []

for i in range(0, 15):
    valor = int(input(f'Entre com o {i + 1}° valor: '))
    vetor.append(valor)

print(f'Vetor original: {vetor}')

for item in vetor:  # remoção de elementos em uma lista de forma iterada (ou seja, em um loop)
    if item == 0:
        vetor.remove(item)

print(f'Vetor sem zeros: {vetor}')

