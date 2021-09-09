"""
Questão 13
"""
vetor = []
valor = 0

for i in range(0, 5):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    vetor.append(valor)

print(f'O vetor informado possui as seguinte componente: {vetor}')
print(f'A posição do menor valor é {vetor.index(min(vetor))}, o maior valor é {vetor.index(max(vetor))}.')
