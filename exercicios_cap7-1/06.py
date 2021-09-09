"""
Questão 06
"""
vetor = []
valor = 0
print('Entre com os valores do vetor de 10 elementos:')
for i in range(0, 10):
    valor = int(input(f'Entre com {i+1}: '))
    vetor.append(valor)

print(f'O vetor tem valor mínimo {min(vetor)} e máximo {max(vetor)}.')
