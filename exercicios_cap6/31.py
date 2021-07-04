"""
Questão 31
"""
n = int(input('Entre com o valor: '))
S = 0
for i in range(1, n + 1):
    S += ((2*i - 1) / i)
print(f'A primeira série é: {S}\n')
