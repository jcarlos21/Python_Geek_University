"""
Questão 30
"""
v1 = []
v2 = []
v3 = []
valor = 0
soma, carlos = 1, 2  # lembre-se que a maneira correta de se criar duas variáveis em uma linha é essa

for i in range(0, 10):
    valor = int(input(f'Entre com o {i + 1}° valor do primeiro vetor: '))
    v1.append(valor)
    valor = int(input(f'Entre com o {i + 1}° valor do segundo vetor: '))
    v2.append(valor)

for j in range(0, len(v1)):
    for m in range(0, len(v2)):
        if v1[j] == v2[m] and v3.count(v1[j]) == 0:
            v3.append(v1[j])

v3.sort()
print(f'O vetor 3 é: {v3}')
