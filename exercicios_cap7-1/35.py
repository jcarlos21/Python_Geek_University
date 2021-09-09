"""
Questão 35
"""

a = int(input(f'Entre com um número maior que 0 e menor que 10000: '))
b = int(input(f'Entre com um número maior que 0 e menor que 10000: '))

vetor_a = []
vetor_b = []

a_n = a
b_n = b

mod = 0

i = 0
while a > 0:
    mod = a % 10
    vetor_a.append(mod)
    a = a // 10

i = 0
mod = 0
while b > 0:
    mod = b % 10
    vetor_b.append(mod)
    b = b // 10

vetor_c = []

if a_n < b_n:
    print('Estou no if')
    for j in range(0, len(vetor_a)):
        vetor_c.append(vetor_a[j] + vetor_b[j])
        if j == len(vetor_a) - 1 and len(vetor_a) != len(vetor_b):
            vetor_c.append(vetor_b[len(vetor_a)])
else:
    print('Estou no else')
    for j in range(0, len(vetor_b)):
        vetor_c.append((vetor_a[j] + vetor_b[j]))
        if j == len(vetor_b) - 1 and len(vetor_a) != len(vetor_b):
            vetor_c.append(vetor_a[len(vetor_b)])

print(f'\nVetor a: {vetor_a}'
      f'\nVetor b: {vetor_b}'
      f'\nVetor c: {vetor_c}')
