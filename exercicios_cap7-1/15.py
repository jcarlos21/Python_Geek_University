"""
Questão 15
"""
vetor = []
valor = 0

for i in range(0, 20):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    if vetor.count(valor) == 0:
        vetor.append(valor)

vetor.sort()
print(f'O vetor é: {vetor}')

