"""
Questão 04
"""
print('Entre com valores para um vetor de 8 elementos: ')
vetor = []
valor = 0
for i in range(0, 8):
    valor = float(input(f'Entre com o {i+1}° valor: '))
    vetor.append(valor)

soma = 0
print('Agora escolha duas posições do vetor para somá-las:')
for g in range(0, 2):
    valor = int(input(f'Posição {g+1}: '))
    soma += vetor[valor-1]

print(f'\nO resultado da soma é: {soma}')
