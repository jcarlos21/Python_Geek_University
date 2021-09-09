"""
Questão 05
"""
matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = int(input(f'Entre com o valor da posição [{l}, {c}]: '))

X = int(input('\nEntre com um número para procurar na matriz: '))
busca = False
for i in range(0, 5):
    for j in range(0, 5):
        if X == matriz[i][j]:
            busca = True
            break
    if busca:
        break

if busca:
    print(f'\nO número digitado está na posição [{i}, {j}]')
else:
    print(f'\nO valor {X} não foi encontrado na matriz.')
