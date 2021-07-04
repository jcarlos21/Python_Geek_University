"""
Questão 28
"""
n = int(input('Entre com o valor: '))
fat = 1
"""
if n == 0:
    fat = 1
else:
    for g in range(1, n + 1):
        fat = fat * g
"""
E = 1
for i in range(1, n + 1):
    fat *= i
    E += (1 / fat)
print(f'A série tende a {E}.')
