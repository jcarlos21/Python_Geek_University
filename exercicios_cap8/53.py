"""
Questão 53
"""


def GeraMatriz(linha, coluna):
    matriz = []
    laco = 0
    while laco < linha:
        matriz.append([])
        laco += 1
    for a in range(0, linha):
        for b in range(0, coluna):
            matriz[a].append([])
    return matriz


def PreencheMatriz(x):
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            x[a][b] = int(input(f'Entre com o elemento da posição [{a}, {b}]: '))
    return x


def EhMatrizIdentidade(x):
    cont = 0
    cont2 = 0
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            if a == b and x[a][b] == 1:
                cont += 1
            else:
                if x[a][b] == 0:
                    cont2 += 1
    if (cont == len(x[0])) and (cont2 == len(x)):
        return True
    return False


linhas = colunas = int(input('Entre com o número de linhas e colunas para a matriz quadrática: '))
A = GeraMatriz(linhas, colunas)
B = PreencheMatriz(A)
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{B[i][j]:^3}', end='')
    print()

if EhMatrizIdentidade(B):
    print('A matriz digitada é matriz identidade.')
else:
    print('A matriz digitada é não matriz identidade.')

print(len(B[0]))
print(len(B))
