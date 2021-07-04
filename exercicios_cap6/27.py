"""
Questão 27
"""
n = int(input('Entre com o valor: '))
H = 0
for i in range(1, n + 1):
    H += (1 / i)
print(f'A série harmônica é igual a {H}.')
