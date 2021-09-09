"""
Questão 14
"""
vetor = []
valor = igual = 0

for i in range(0, 10):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    vetor.append(valor)

for j in range(0, 10):
    igual = vetor.count(j)
    if igual >= 2:
        print(f'Há {igual} ocorrências do valor {vetor[vetor.index(j)]}.')
        igual = 0
    igual = 0

