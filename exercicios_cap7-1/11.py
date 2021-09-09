"""
Questão 11
"""
vetor = []
valor = soma = cont = 0

for i in range(0, 10):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    vetor.append(valor)
    if vetor[i] > 0:
        soma += vetor[i]
    if vetor[i] < 0:
        cont += 1

print(f'Houve {cont} entradas negativas para o vetor informado.')
print(f'A soma das entradas positivas do vetor informado é: {soma}.')
