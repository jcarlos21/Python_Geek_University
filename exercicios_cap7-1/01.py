"""
Questão 01
"""

VetorA = []
vetor = 0
soma = 0

print('Entre com o valores inteiros do vetor A: ')
for i in range(0, 6):
    vetor = int(input(f'{i+1}° valor: '))
    VetorA.append(vetor)
    if i == 0 or i == 1 or i == 5:
        soma += VetorA[i]
print(f'A soma dos inteiros das posições 0, 1 e 5 é: {soma}')

vetor = int(input('Entre com o novo valor da posição 4 do vetor: '))
VetorA[4] = vetor

print('Novo vetor:')
for g in VetorA:
    print(g)

