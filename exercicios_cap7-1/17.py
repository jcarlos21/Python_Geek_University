"""
Questão 17
"""
vetor = []
valor = 0

for i in range(0, 10):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    if valor < 0:
        vetor.append(0.0)
    else:
        vetor.append(valor)
print(f'\nO vetor digitado é: {vetor}')