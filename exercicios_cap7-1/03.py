"""
Questão 03
"""
vetor = []
valor = 0
vetorQ = []
quadrado = 0
print('Alimente o vetor com 10 elementos: ')
for i in range(0, 10):
    valor = float(input(f'Valor {i+1}: '))
    vetor.append(valor)
    vetorQ.append(vetor[i] ** 2)


print(f'O vetor quadrado é: {vetorQ}')


