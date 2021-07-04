"""
Questão 33
"""
n = int(input('Entre com o valor: '))
a = int(input('Entre com um valor diferente de zero: '))
b = int(input('Entre com outro valor diferente de zero: '))
cont = 1
i = 0
while cont <= n:
    if i % a == 0 or i % b == 0:
        if i == 0:
            print(f'Os múltiplos de {a} e {b} são: {i}, ', end='')
        else:
            if cont == n:
                print(i, end='.')
            else:
                print(i, end=', ')
        cont += 1
    i += 1
