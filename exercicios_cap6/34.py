"""
Questão 34
"""
n = int(input('Entre com o valor: '))
cont = 0
num = 1
i = 1
while True:
    i = 1
    while i <= n:
        if num % i == 0:
            cont += 1
        i += 1
    if cont < n:
        cont = 0
    if cont == n:
        break
    else:
        print(num)
        num += 1

print(num, cont)
