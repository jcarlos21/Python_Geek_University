"""
Questão 58
"""

a = int(input('Entre com um número inteiro: '))
b = int(input('Entre com um número inteiro: '))
cont = 0
soma = 0

for i in range(a, b + 1):  # Vezes que o laço vai rodar
    cont = 0
    for j in range(1, i + 1):  # Laço responsável pela verificação de cada número do intervalo (a, b)
        if i % j == 0:
            cont += 1
    if cont == 2 or cont == 1:
        soma += i

print(f'Entre {a} e {b} a soma dos números primos é: {soma}')
