"""
Questão 22
"""
vetor = []
vetor2 = []
valor = 0
vetor3 = []
for i in range(0, 10):
    valor = int(input(f'Entre com {i+1}° valor inteiro do vetor 1: '))
    vetor.append(valor)
    valor = int(input(f'Entre com {i+1}° valor inteiro do vetor 2: '))
    vetor2.append(valor)

for j in range(0, 10):
    vetor3.append(vetor[j])
    vetor3.append(vetor2[j])

print(f'O vetor 3 é: {vetor3}')
