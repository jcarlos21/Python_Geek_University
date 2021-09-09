"""
Questão 38
"""
vetor = []
valor = 0
for i in range(0, 10):
    valor = int(input(f'Entre com o {i + 1}° valor: '))
    vetor.append(valor)
    vetor.sort()
print(f'O vetor digitado é: {vetor}')
