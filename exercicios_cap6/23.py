"""
Questão 23
"""
num = int(input('Entre com um número inteiro positivo: '))
for i in range(1, num+1):
    if num % i == 0:
        if i == 1:
            print(f'Os divisores de {num} são: ', end='')
        if i == num:
            print(i, end='.')
        else:
            print(i, end=', ')
