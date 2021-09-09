"""
Questão 08
"""
vetor = []
valor = 0
print('Entre com os valores do vetor de 6 elementos:')
for i in range(0, 6):
    valor = int(input(f'Entre com {i+1}: '))
    vetor.append(valor)

print(f'O vetor na ordem inversa é: {vetor[::-1]}.')
