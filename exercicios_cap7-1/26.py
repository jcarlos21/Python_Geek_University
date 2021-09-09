"""
Questão 26
"""
import math
vetor = []
valor = soma = 0

for i in range(0, 10):
    valor = int(input(f'Entre com o {i+1}° valor: '))
    vetor.append(valor)

m = sum(vetor) / len(vetor)
for j in range(0, len(vetor)):
    soma += (vetor[j] - m) ** 2

DesvioPadrao = math.sqrt((1 / (len(vetor) - 1)) * soma)

print(f'O desvio padrão é: {DesvioPadrao}')
