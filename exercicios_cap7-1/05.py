"""
Questão 05
"""
vetor = []
valor = 0
par = []
cont = 0
print('Entre com os valores do vetor de 10 elementos:')
for i in range(0, 10):
    valor = int(input(f'Entre com {i+1}: '))
    vetor.append(valor)
    if vetor[i] % 2 == 0:
        cont += 1
        par.append(vetor[i])
print(f'O vetor par é {par} e teve {cont} entradas.')
