"""
Questão 09
"""
N = int(input('Entre com um número inteiro: '))
cont = i = 0
while i < N or cont != N:
    if i % 2 == 1:
        print(i)
        cont += 1
    i += 1
