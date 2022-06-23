"""
Questão 73
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


# A pesquisa conta com 4 perguntas que serão o número de colunas da matriz de dados


def Perguntas(n):
    if n == 0:
        sexo = input('Entre com o sexo (M - masculino, F - feminino): ')
        return sexo.title()
    elif n == 1:
        cor_dos_olhos = input('Entre com a cor dos olhos (A - azuis ou C - castanhos): ')
        return cor_dos_olhos.title()
    elif n == 2:
        cor_dos_cabelos = input('Entre com a cor dos cabelos (L - louro, P - presto ou C - castanhos): ')
        return cor_dos_cabelos.title()
    else:
        idade = int(input('Entre com a idade: '))
        return idade


def PreenchimenmtoMatrizDados(linha):
    matriz_de_dados = GeraMatriz(linha, 4)
    for a in range(0, linha):
        print(f'{a+1}ª pessoa')
        for b in range(0, 4):
            matriz_de_dados[a][b] = Perguntas(b)
        print()
    return matriz_de_dados


# Funcções pedidas nas questões


def MediaIdade(matriz):
    soma = 0
    for a in range(0, len(matriz)):
        soma += matriz[a][3]
    return soma / 4


def MaiorIdade(matriz):
    maior = 0
    for a in range(0, len(matriz)):
        if matriz[a][3] > maior:
            maior = matriz[a][3]
    return maior


def Selecao(m):
    cont = 0
    for a in range(0, len(m)):
        if m[a][0] == 'F' and m[a][1] == 'A' and m[a][2] == 'L' and (18 <= m[a][3] <= 35):
            cont += 1
    return cont


# A quantidade de pessoas representará a quantidade de linhas da matriz de dados
qtd_pessoas = int(input('Entre com a quantidade de pessoas da pesquisa: '))
print()
pesquisa = PreenchimenmtoMatrizDados(qtd_pessoas)

print(f'\nA média de idade é: {MediaIdade(pesquisa)}')
print(f'A maior idade é: {MaiorIdade(pesquisa)}')
print(f'A quantidade de mulheres, cuja a idade está entre 18 e 35 anos e que possuem '
      f'olhos azuis e cabelos louros é: {Selecao(pesquisa)}')
