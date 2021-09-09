"""
Questão 29
"""
vetor = []
valor = 0

for i in range(0, 6):
    valor = int(input(f'Entre com o {i+1}° valor: '))
    vetor.append(valor)

pares = []
Impares = []
SomaPares = cont = 0

for j in range(0, len(vetor)):
    if vetor[j] % 2 == 0:
        pares.append(vetor[j])
        SomaPares += vetor[j]
    else:
        Impares.append(vetor[j])
        cont += 1

print(f'\nNúmeros pares digitados: {pares}'
      f'\nSoma dos números pares digitados: {SomaPares}'
      f'\nNúmeros ímpares digitados: {Impares}'
      f'\nQuantidade de números ímpares digitados: {cont}')
