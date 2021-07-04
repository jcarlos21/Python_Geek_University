"""
Questão 56
"""
cont = 0
soma = 0
a = 1
i = 0
while i < 2000000:
    cont = 0
    for j in range(1, a+1):
        if a % j == 0:
            cont += 1
    if cont == 2 or cont == 1:
        soma += a
        print(a)
        i += 1
    a += 1

print(f'A soma dos números primos abaixo de 2 milhões é: {soma}')
