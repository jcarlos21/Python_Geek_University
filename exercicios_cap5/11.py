"""
Questão 11
"""
num = int(input('Entre com um numero inteiro para fazer a soma de seus algarismos: '))
soma = 0
while num != 0:
    soma = soma + (num % 10)
    num = num // 10
print(f'A soma dos algarismo de {num} é: {soma}')
