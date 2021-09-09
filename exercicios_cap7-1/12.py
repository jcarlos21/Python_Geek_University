"""
Questão 12
"""
vetor = []
valor = 0

for i in range(0, 5):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    vetor.append(valor)

print(f'O vetor informado possui as seguinte componente: {vetor}')
print(f'O menor valor é {min(vetor)}, o maior valor é {max(vetor)} e a media dos valores é {sum(vetor) / len(vetor)}.')
