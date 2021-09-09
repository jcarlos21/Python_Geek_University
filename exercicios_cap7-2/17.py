"""
Questão 17
"""
import random
matriz = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0],
          [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
num = 0.0
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        num = random.uniform(4, 10)  # esse comando gera numeros aleatório do tipo float
        matriz[i][j] = num.__round__(2)

pior = 100.0
qtd_notas_ruim = [0, 0, 0]
m = -1
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        if matriz[i][j] < pior:
            pior = matriz[i][j]
            m = j
    if m == 0:
        qtd_notas_ruim[0] += 1
    elif m == 1:
        qtd_notas_ruim[1] += 1
    else:
        qtd_notas_ruim[2] += 1
    pior = 100.00

print(f'As notas foram:'
      f'\n{matriz}\n')

for i in range(0, len(qtd_notas_ruim)):
    print(f'A prova {i+1} teve {qtd_notas_ruim[i]} notas ruins.')
