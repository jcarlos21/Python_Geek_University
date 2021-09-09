"""
Questão 19
"""
vetor = []
valor = 0
for i in range(0, 50):
    valor = (i + 5 * i) % (i + 1)
    vetor.append(valor)

print(f'\nO vetor é: {vetor}')
