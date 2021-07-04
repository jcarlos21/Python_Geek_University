"""
Questão 24
"""
num = int(input('Entre com um número inteiro positivo: '))
soma = 0
for i in range(1, num):
    if num % i == 0:
        soma += i
print(f'A soma dos divisores de {num} é: {soma}')
