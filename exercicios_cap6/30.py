"""
Questão 30
"""
n = int(input('Entre com o valor: '))
soma = 0
for i in range(1, n + 1):
    soma += i
print(f'A primeira série é: {soma}\n')

soma2 = 0
for g in range(1, n + 1):
    soma2 += (((2 * g) - 1) - (2 * g))
print(f'A segunda série é: {soma2}\n')

soma3 = 0
for h in range(1, n + 1):
    soma3 += (2*h - 1)
print(f'A terceira série é: {soma3}\n')
