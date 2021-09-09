"""
Questão 21
"""
vetor = []
vetor2 = []
valor = 0
for i in range(0, 10):
    valor = int(input(f'Entre com {i+1}° valor inteiro do vetor 1: '))
    vetor.append(valor)
    valor = int(input(f'Entre com {i+1}° valor inteiro do vetor 2: '))
    vetor2.append(valor)

vetor3 = []
for j in range(0, 10):
    vetor3.append(vetor[j] - vetor2[j])

print(f'O vetor gerado por {vetor} menos {vetor2} é: {vetor3}.')
