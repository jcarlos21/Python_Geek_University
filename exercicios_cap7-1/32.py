"""
Questão 32
"""
x = []
y = []
soma = 0
valor = 0
produto = 0
diferenca = []
intersecao = []
uniao = []

for i in range(0, 5):
    valor = int(input(f'Entre com o {i + 1}° valor do vetor x: '))
    x.append(valor)
    valor = int(input(f'Entre com o {i + 1}° valor do vetor y: '))
    y.append(valor)

    soma += x[i] + y[i]

    produto += x[i] * y[i]

    if y.count(x[i]) == 0:
        diferenca.append(x[i])

    if uniao.count(x[i]) == 0:
        uniao.append(x[i])
    if uniao.count(y[i]) == 0:
        uniao.append(y[i])

for m in range(0, len(x)):  # intersecao
    for j in range(0, len(y)):
        if x[m] == y[j] and intersecao.count(x[m]) == 0:
            intersecao.append(x[m])

diferenca.sort()
intersecao.sort()
uniao.sort()

print(f'\nA soma dos elementos de cada posição é: {soma}'
      f'\nA soma do produtos de cada valor em cada posição é: {produto}'
      f'\nA diferença entre x e y é: {diferenca}'
      f'\nA interseção entre x e y é: {intersecao}'
      f'\nA união de x e y (sem repetições) é: {uniao}')
