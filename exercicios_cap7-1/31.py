"""
Questão 31
"""
v1 = []
v2 = []
v3 = []
valor = 0

for i in range(0, 10):
    valor = int(input(f'Entre com o {i + 1}° valor do primeiro vetor: '))
    v1.append(valor)
    valor = int(input(f'Entre com o {i + 1}° valor do segundo vetor: '))
    v2.append(valor)

for j in range(0, len(v1)):
    if v3.count(v1[j]) == 0:
        v3.append(v1[j])
    if v3.count((v2[j])) == 0:
        v3.append(v2[j])

v3.sort()
print(f'\nO vetor 3 sem repetições é: {v3}')
