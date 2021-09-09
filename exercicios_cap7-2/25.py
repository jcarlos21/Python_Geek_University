"""
Questão 25 - Jogo da velha
"""
import random

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jogador01 = 0
jogador02 = 0
fimdejogo = 1
iniciar = 0
p = 0  # posição recebida pelo jogador
a = 0
b = 0
print('BEM-VINDO AO JOGO DA VELHA!\n')


# Funções:___________________________________________________________________________
def posicao_matriz(x):
    if x == 1:
        return 0, 0
    elif x == 2:
        return 0, 1
    elif x == 3:
        return 0, 2
    elif x == 4:
        return 1, 0
    elif x == 5:
        return 1, 1
    elif x == 6:
        return 1, 2
    elif x == 7:
        return 2, 0
    elif x == 8:
        return 2, 1
    else:
        return 2, 2


def SituacaoMatriz(M, linha, coluna):
    cont = 0
    for i in range(0, linha):
        for j in range(0, coluna):
            if M[i][j] != 0:
                cont += 1
    if cont == 9:
        return True
    else:
        return False


def situacao(M, num_jogador):
    if M[0][0] == M[1][1] == M[2][2] == num_jogador:
        return True
    elif M[0][2] == M[1][1] == M[2][0] == num_jogador:
        return True
    elif M[0][0] == M[0][1] == M[0][2] == num_jogador:
        return True
    elif M[1][0] == M[1][1] == M[1][2] == num_jogador:
        return True
    elif M[2][0] == M[2][1] == M[2][2] == num_jogador:
        return True
    elif M[0][0] == M[1][0] == M[2][0] == num_jogador:
        return True
    elif M[0][1] == M[1][1] == M[2][1] == num_jogador:
        return True
    elif M[0][2] == M[1][2] == M[2][2] == num_jogador:
        return True
    else:
        return False


def impressao(M):
    for i in range(0, len(M)):
        for j in range(0, len(M)):
            print(f'{M[i][j]:^3}', end='')
        print()


# Início do jogo_____________________________________________________________________
while iniciar != 1 and iniciar != -1:
    iniciar = random.randint(-1, 1)

print('O JOGO COMEÇOU!\n')
if iniciar == 1:
    impressao(matriz)
    print()
    print('Jogador 1 começa e jogará com o número 1!\n')
else:
    impressao(matriz)
    print()
    print('Jogador 2 começa e jogará com o número -1!\n')

# Laço do jogo_______________________________________________________________________
while fimdejogo != 0:  # laço do jogo

    if iniciar == 1:
        p = int(input('Jogador 1 escolha uma posição de 1 a 9 para alocar o número 1: '))
        a, b = posicao_matriz(p)
        while matriz[a][b] != 0:  # verificando se a posição [a, b] está vazia
            p = int(input('\nPosição já possui um número alocado. Selecione outra posição: '))
            a, b = posicao_matriz(p)

        matriz[a][b] = 1
        iniciar = -1  # condição para o proximo jogador jogar
        print()
        impressao(matriz)
        print()
        if situacao(matriz, 1):  # função de situação da matriz
            fimdejogo = 0
            print('O jogador 1 ganhou!!!')
    else:
        p = int(input('Jogador 2 escolha uma posição de 1 a 9 para alocar o número -1: '))
        a, b = posicao_matriz(p)
        while matriz[a][b] != 0:  # verificando se a posição [a, b] está vazia
            p = int(input('\nPosição já possui um número alocado. Selecione outra posição: '))
            a, b = posicao_matriz(p)

        matriz[a][b] = -1
        iniciar = 1  # condição para o proximo jogador jogar
        print()
        impressao(matriz)
        print()
        if situacao(matriz, -1):  # função de situação da matriz
            fimdejogo = 0
            print('O jogador 2 ganhou!!!')

    # tem que fazer dois laços "for" para procurar por zero na matriz e encerrar o jogo.
    if SituacaoMatriz(matriz, len(matriz), len(matriz)):
        fimdejogo = 0
        print('\nHOUVE EMPATE! FIM DE JOGO!')
