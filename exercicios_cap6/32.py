"""
Questão 32
"""
import random
n = int(input('Entre com a quantidade de vezes que os dados serão lançados: '))
d1 = random.randint(0, 6)
d2 = random.randint(0, 6)

for i in range(1, n + 1):
    d1 = random.randint(0, 6)
    d2 = random.randint(0, 6)
    if d1 > d2:
        print(f'Os dados foram {d1} e {d2} respectivamente. O dado 1 é maior que o dado 2.')
    else:
        print(f'Os dados foram {d1} e {d2} respectivamente. O dado 2 é maior que o dado 1.')
