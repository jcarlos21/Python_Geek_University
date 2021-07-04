"""
Questão 54
"""
n = int(input('Entre com um número inteiro: '))
cont = 0

for i in range(1, n+1):
    if n % i == 0:
        cont += 1

if cont == 2 or cont == 1:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
