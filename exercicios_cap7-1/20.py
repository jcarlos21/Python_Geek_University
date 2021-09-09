"""
Questão 20
"""
import random

vetor = []
valor = 0
for i in range(0, 10):
    valor = random.randint(0, 50)
    vetor.append(valor)
vetor2 = []
for j in range(0, 10):
    if not vetor[j] % 2 == 0:
        vetor2.append(vetor[j])

for m in range(0, 10, 2):
    if m + 1 != 10:
        print(f'{vetor[m]}, {vetor[m+1]}')
    else:
        print(f'{vetor[m]}')

print()
for n in range(0, len(vetor2), 2):
    if n + 1 != len(vetor2):
        print(f'{vetor2[n]}, {vetor2[n+1]}')
    else:
        print(f'{vetor2[n]}')

print(f'\nO vetor é: {vetor}')
print(f'\nO vetor é: {vetor2}')

