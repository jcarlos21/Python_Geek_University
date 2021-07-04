"""
Questão 18
"""
N = int(input('Entre a quantidade de números que será lido pelo programa: '))
num = 0
maior = cont = 0
lista = []
for i in range(0, N):
    num = int(input(f'Entre com o {i+1}° número: '))
    lista.append(num)
    if i == 0:
        maior = num
    elif num > maior:
        maior = num

for g in lista:  # listas não faz parte da seção 6
    if maior == g:
        cont += 1

print(f'O maior número é {maior} e foi lido {cont} vezes.')
