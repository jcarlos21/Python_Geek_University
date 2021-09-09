"""
Questão 23
"""
vetor = []
vetor2 = []
valor = 0
ProdutoEscalar = 0
for i in range(0, 10):
    valor = float(input(f'Entre com {i+1}° valor real do vetor 1: '))
    vetor.append(valor)
    valor = float(input(f'Entre com {i+1}° valor real do vetor 2: '))
    vetor2.append(valor)

for j in range(0, 10):
    ProdutoEscalar += vetor[j] * vetor2[j]

print(f'\nO vetor 1 é: {vetor}')
print(f'O vetor 2 é: {vetor2}')
print(f'\nO produto escalar entre as componentes do vetor é: {ProdutoEscalar}')
