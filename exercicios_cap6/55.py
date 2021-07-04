"""
Questão 55
"""
n = int(input('Entre com um número inteiro: '))
cont = 0
soma = 0
a = 1
i = 0
while i < n:
    cont = 0
    for j in range(1, a+1):
        if a % j == 0:
            cont += 1
    if cont == 2 or cont == 1:
        soma += a
        i += 1
    a += 1

print(f'A soma dos {n} primeiros primos é: {soma}')
