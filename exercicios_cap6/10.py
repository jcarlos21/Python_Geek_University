"""
Questão 10
"""
N = int(input('Entre com um número inteiro: '))
soma = cont = i = 0
while i < N or cont != N:
    if i % 2 == 0 and i != 0:
        soma = soma + i
        cont += 1
    i += 1
print(f'A soma dos {N} primeiro números pares é: {soma}')
