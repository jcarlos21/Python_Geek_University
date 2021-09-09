"""
Questão 28
"""
vetor = []
valor = 0

for i in range(0, 10):
    valor = int(input(f'Entre com o {i+1}° valor: '))
    vetor.append(valor)

v1 = []
v2 = []

for j in range(0, len(vetor)):
    if not vetor[j] % 2 == 0:
        v1.append(vetor[j])
    else:
        v2.append(vetor[j])

print(f'Os valores ímpares são: {v1}'
      f'\nOs valores pares são: {v2}')
