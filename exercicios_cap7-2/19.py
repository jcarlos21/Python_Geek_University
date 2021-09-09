"""
Questão 19
"""
import random

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matricula = 1250
num = 0.0
maior_media_final = -1000000.0
matricula_maior_media_final = 124
soma_nota_final = 0.0

for i in range(0, 5):
    num = 0.0
    for j in range(0, 4):
        if j == 0:
            matricula += 1
            matriz[i][j] = matricula
        elif j == 1:  # médias das provas
            num = random.uniform(5, 10)
            matriz[i][j] = num.__round__(2)
            num = 0.0
        elif j == 2:  # médias dos trabalhos
            num = random.uniform(5, 10)
            matriz[i][j] = num.__round__(2)
        else:  # nota final
            matriz[i][j] = (matriz[i][1] + matriz[i][2]).__round__(2)
            if matriz[i][j] > maior_media_final:
                maior_media_final = matriz[i][j]
                matricula_maior_media_final = matricula
            soma_nota_final += matriz[i][j]

print('\nA matriz gerada é:\n')
for i in range(0, 5):
    for j in range(0, 4):
        print(f'{matriz[i][j]:^7}', end='')
    print()

print(f'\nMaior nota: {maior_media_final}'
      f'\nMatrícula: {matricula_maior_media_final}'
      f'\nMédia aritmética: {(soma_nota_final / len(matriz)).__round__(2)}')
